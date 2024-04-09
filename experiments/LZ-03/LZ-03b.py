from rp2040hw.pio import pios, clkdiv
from pico_ctrlaer import ON, OFF, mux, CtrlAer
from machine import Pin, ADC
import time

adc = ADC(Pin(26))

def prog1():
    for i in range(1200):
        reading = adc.read_u16()
        freq = 106_500 + (reading >> 3)
        ctrlaers[0].set_freq(freq)
        print(i, freq)
        yield ON, 100
        yield OFF, 250

def prog2():
    for i in range(1200):
       yield ON, 40
       yield OFF, 260

# GP0: Alginate 0.25%, 0.025 M sodium ferrocyanide
# GP1: CaCl2 (1%) solution, 0.025 M FeCl3 solution
progs = [
    mux([prog1()]),
    # mux([prog2()]),

]
ctrlaers = [
    CtrlAer(sm_number=0, base_pin=0, n_pins=1, freq=110_600),
    # CtrlAer(sm_number=1, base_pin=1, n_pins=1, freq=114_000)
]

while True:
    for i, (ctrlaer, prog) in enumerate(zip(ctrlaers, progs)):
        ctrlaer.run(prog, block=False)
