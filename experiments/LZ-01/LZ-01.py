import sys
sys.path.insert(0, '/HM-B1-10-11-23/pico_ctrlaer')

from pico_ctrlaer import ON, OFF, mux, CtrlAer

def prog1():
    for i in range(600):
        yield ON, 50
        yield OFF, 2000

# GP25: Pi Pico onboard LED
# GP26: RuCl3 solution
progs = [prog1(), prog1()]
prog = mux(progs)
ctrlaer = CtrlAer(sm_number=0, base_pin=25, n_pins=len(progs))
ctrlaer.run(prog)
