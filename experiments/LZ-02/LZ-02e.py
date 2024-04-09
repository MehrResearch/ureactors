from rp2040hw.pio import pios, clkdiv
from pico_ctrlaer import ON, OFF, mux, CtrlAer
from machine import Pin
import time

def prog1():
    for i in range(1200):
        print(i)
        yield ON, 50
        yield OFF, 250

def prog2():
    for i in range(1200):
       yield ON, 40
       yield OFF, 260

# GP0: Alginate 0.25%, 0.05 M NaOH, phenolphthalein solution
# GP1: CaCl2 (1%) solution, 0.05 M HCl, bromothymol blue solution 
progs = mux([prog1()]),mux([prog2()])
ctrlaers = [
    CtrlAer(sm_number=0, base_pin=0, n_pins=1, freq=110_500),
    CtrlAer(sm_number=1, base_pin=1, n_pins=1, freq=114_000)
]

while True:
    for i, (ctrlaer, prog) in enumerate(zip(ctrlaers, progs)):
        ctrlaer.run(prog, block=False)
