from rp2040hw.pio import pios, clkdiv
from pico_ctrlaer import ON, OFF, mux, CtrlAer
from machine import ADC, Pin

adc = ADC(Pin(26))

def prog1():
    for i in range(600):
        reading = adc.read_u16()
        freq = 106_500 + (reading >> 3)
        ctrlaer.set_freq(freq)
        print(freq)
        yield ON, 250
        yield OFF, 250

def prog2():
    for i in range(600):
        # yield OFF, 75
        # yield ON, 100
       #  yield OFF, 325
       yield ON, 250
       yield OFF, 250

# GP0: mAlginate solution
# GP1: CaCl2 (2%) solution
progs = [prog1(), prog2()]
prog = mux(progs)
ctrlaer = CtrlAer(sm_number=0, base_pin=0, n_pins=len(progs))
ctrlaer.run(prog)

