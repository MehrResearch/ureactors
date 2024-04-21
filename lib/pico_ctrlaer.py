from machine import Pin
from rp2 import PIO, asm_pio, StateMachine

from rp2040hw.pio import pios, clkdiv

ON = const(1)
OFF = const(0)
FREQ = const(108_050)
RP2040_CLK = const(125_000_000)


def _always_on():
    while True:
        yield ON, 1000


def _inactive():
    # Yielding once is enough: mux() yields OFF when the generator is exhausted.
    # This guarantees that mux() terminates after the last active program.
    yield OFF, 1000


inactive = _inactive()
always_on = _always_on()


def mux(progs):
    N = len(progs)
    default = OFF, 1000
    times = [0] * N
    val = 0
    while True:
        alive = 0
        for i, prog in enumerate(progs):
            if times[i] == 0:
                try:
                    cmd = next(prog)
                    alive += 1
                except StopIteration:
                    cmd = default
                val &= ~(1 << i)
                val |= cmd[0] << i
                times[i] = cmd[1]
        min_time = min(times)
        if not alive:
            break
        yield val, min_time
        for i in range(N):
            times[i] -= min_time


class CtrlAer:
    def __init__(self, sm_number, base_pin, n_pins, freq=FREQ):
        self.n_pins = n_pins
        self._freq = freq
        self.pio = pios[sm_number // 4]
        self.sm_number = sm_number % 4
        self.bit_mask = 1 << self.sm_number
        self.sm_reg = self.pio.SM[self.sm_number]

        @asm_pio(
            out_init=(PIO.OUT_LOW,) * n_pins,
            out_shiftdir=PIO.SHIFT_RIGHT,
            fifo_join=PIO.JOIN_TX,
        )
        def oscillator():
            pull()  # pin states
            mov(x, osr)

            out(pins, n_pins)[4]
            out(pins, n_pins)

            pull()  # duration in ticks (1 tick = 1/freq s)
            mov(y, osr)

            label("loop")
            mov(osr, x)[1]
            out(pins, n_pins)[4]
            out(pins, n_pins)
            jmp(y_dec, "loop")[1]

        self.sm = StateMachine(
            sm_number, oscillator, freq=self._freq * 2 * 5, out_base=Pin(base_pin)
        )
        self.sm.active(1)

    def set_freq(self, freq):
        self._freq = freq
        i, f = clkdiv(freq * 2 * 5, RP2040_CLK)
        self.sm_reg.CLKDIV.INT = i
        self.sm_reg.CLKDIV.FRAC = f
        
    def ticks(self, time):
        return time * self._freq // 1000
    
    def is_full(self):
        return (self.pio.FSTAT.TXFULL & self.bit_mask) >> self.sm_number

    def run(self, prog, block=True):
        put = self.sm.put
        if not block and self.is_full():
            return
        for state, length in prog:
            put(state)
            put(self.ticks(length))
            if not block and self.is_full():
                return
