#    Copyright 2023 Hessam Mehr

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from uctypes import BF_POS, BF_LEN, BFUINT32, ARRAY, UINT32, struct

PIO_BASE = [0x50200000, 0x50300000]

PIO_CTRL_FIELDS = {
    "CLKDIV_RESTART": 8 << BF_POS | 4 << BF_LEN | BFUINT32,
    "SM_RESTART": 4 << BF_POS | 4 << BF_LEN | BFUINT32,
    "SM_ENABLE": 0 << BF_POS | 4 << BF_LEN | BFUINT32,
}

PIO_FSTAT_FIELDS = {
    "TXEMPTY": 24 << BF_POS | 4 << BF_LEN | BFUINT32,
    "TXFULL": 16 << BF_POS | 4 << BF_LEN | BFUINT32,
    "RXEMPTY": 8 << BF_POS | 4 << BF_LEN | BFUINT32,
    "RXFULL": 0 << BF_POS | 4 << BF_LEN | BFUINT32,
}

PIO_FDEBUG_FIELDS = {
    "TXSTALL": 24 << BF_POS | 4 << BF_LEN | BFUINT32,
    "TXOVER": 16 << BF_POS | 4 << BF_LEN | BFUINT32,
    "RXUNDER": 8 << BF_POS | 4 << BF_LEN | BFUINT32,
    "RXSTALL": 0 << BF_POS | 4 << BF_LEN | BFUINT32,
}

PIO_FLVEL_FIELDS = {
    "RX3": 28 << BF_POS | 4 << BF_LEN | BFUINT32,
    "TX3": 24 << BF_POS | 4 << BF_LEN | BFUINT32,
    "RX2": 20 << BF_POS | 4 << BF_LEN | BFUINT32,
    "TX2": 16 << BF_POS | 4 << BF_LEN | BFUINT32,
    "RX1": 12 << BF_POS | 4 << BF_LEN | BFUINT32,
    "TX1": 8 << BF_POS | 4 << BF_LEN | BFUINT32,
    "RX0": 4 << BF_POS | 4 << BF_LEN | BFUINT32,
    "TX0": 0 << BF_POS | 4 << BF_LEN | BFUINT32,
}

DBG_CFGINFO_FIELDS = {
    "IMEM_SIZE": 16 << BF_POS | 6 << BF_LEN | BFUINT32,
    "SM_COUNT": 8 << BF_POS | 4 << BF_LEN | BFUINT32,
    "FIFO_DEPTH": 0 << BF_POS | 6 << BF_LEN | BFUINT32,
}

CLKDIV_FIELDS = {
    "INT": 16 << BF_POS | 16 << BF_LEN | BFUINT32,
    "FRAC": 8 << BF_POS | 8 << BF_LEN | BFUINT32,
}

EXECCTRL_FIELDS = {
    "EXEC_STALLED": 31 << BF_POS | 1 << BF_LEN | BFUINT32,
    "SIDE_EN": 30 << BF_POS | 1 << BF_LEN | BFUINT32,
    "SIDE_PINDIR": 29 << BF_POS | 1 << BF_LEN | BFUINT32,
    "JMP_PIN": 24 << BF_POS | 5 << BF_LEN | BFUINT32,
    "OUT_EN_SEL": 19 << BF_POS | 5 << BF_LEN | BFUINT32,
    "INLINE_OUT_EN": 18 << BF_POS | 1 << BF_LEN | BFUINT32,
    "OUT_STICKY": 17 << BF_POS | 1 << BF_LEN | BFUINT32,
    "WRAP_TOP": 12 << BF_POS | 5 << BF_LEN | BFUINT32,
    "WRAP_BOTTOM": 7 << BF_POS | 5 << BF_LEN | BFUINT32,
    "STATUS_SEL": 4 << BF_POS | 1 << BF_LEN | BFUINT32,
    "STATUS_N": 0 << BF_POS | 4 << BF_LEN | BFUINT32,
}

SHIFTCTRL_FIELDS = {
    "FJOIN_RX": 31 << BF_POS | 1 << BF_LEN | BFUINT32,
    "FJOIN_TX": 30 << BF_POS | 1 << BF_LEN | BFUINT32,
    "PULL_THRESH": 25 << BF_POS | 5 << BF_LEN | BFUINT32,
    "PUSH_THRESH": 20 << BF_POS | 5 << BF_LEN | BFUINT32,
    "OUT_SHIFTDIR": 19 << BF_POS | 1 << BF_LEN | BFUINT32,
    "IN_SHIFTDIR": 18 << BF_POS | 1 << BF_LEN | BFUINT32,
    "AUTOPULL": 17 << BF_POS | 1 << BF_LEN | BFUINT32,
    "AUTOPUSH": 16 << BF_POS | 1 << BF_LEN | BFUINT32,
}

PINCTRL_FIELDS = {
    "SIDESET_COUNT": 29 << BF_POS | 3 << BF_LEN | BFUINT32,
    "SET_COUNT": 26 << BF_POS | 3 << BF_LEN | BFUINT32,
    "OUT_COUNT": 20 << BF_POS | 6 << BF_LEN | BFUINT32,
    "IN_BASE": 15 << BF_POS | 5 << BF_LEN | BFUINT32,
    "SIDE_BASE": 10 << BF_POS | 5 << BF_LEN | BFUINT32,
    "SET_BASE": 5 << BF_POS | 5 << BF_LEN | BFUINT32,
    "OUT_BASE": 0 << BF_POS | 5 << BF_LEN | BFUINT32,
}

SM_FILEDS = {
    "CLKDIV": (0x00, CLKDIV_FIELDS),
    "EXECCTRL": (0x04, EXECCTRL_FIELDS),
    "SHIFTCTRL": (0x08, SHIFTCTRL_FIELDS),
    "ADDR": (0x0C | ARRAY, 4 | 4 << BF_LEN | BFUINT32),
    "INSTR": (0x10 | ARRAY, 4 | 16 << BF_LEN | BFUINT32),
    "PINCTRL": (0x14, PINCTRL_FIELDS),
}


INTR_FIELDS = {
    "SM": 8 << BF_POS | 4 << BF_LEN | BFUINT32,
    "TXNFULL": 4 << BF_POS | 4 << BF_LEN | BFUINT32,
    "RXNEMPTY": 0 << BF_POS | 4 << BF_LEN | BFUINT32,
}

IRQ_FIELDS = {
    "INTE": (0x00, INTR_FIELDS),
    "INTF": (0x04, INTR_FIELDS),
    "INTS": (0x08, INTR_FIELDS),
}

PIO_REGS = {
    "CTRL": (0x000, PIO_CTRL_FIELDS),
    "FSTAT": (0x004, PIO_FSTAT_FIELDS),
    "FDEBUG": (0x008, PIO_FDEBUG_FIELDS),
    "FLEVEL": (0x00C, PIO_FLVEL_FIELDS),
    "TXF": (0x010 | ARRAY, 4 | UINT32),
    "RXF": (0x020 | ARRAY, 4 | UINT32),
    "IRQ": 0x030 | 0 << BF_POS | 8 << BF_LEN | BFUINT32,
    "IRQ_FORCE": 0x034 | 0 << BF_POS | 8 << BF_LEN | BFUINT32,
    "INPUT_SYNC_BYPASS": 0x038 | BFUINT32,
    "DBG_PADOUT": 0x03C | BFUINT32,
    "DBG_PADOE": 0x040 | BFUINT32,
    "DBG_CFGINFO": (0x044, DBG_CFGINFO_FIELDS),
    "INSR_MEM": (0x048 | ARRAY, 32, 16 << BF_LEN | BFUINT32),
    "SM": (0x0C8 | ARRAY, 4, SM_FILEDS),
    "INTR": (0x128, INTR_FIELDS),
    "IRQ": (0x12C | ARRAY, 2, IRQ_FIELDS),
    "IRQ0": (0x12C, IRQ_FIELDS),
    "IRQ1": (0x138, IRQ_FIELDS),
}

pios = [struct(addr, PIO_REGS) for addr in PIO_BASE]

def clkdiv(target_freq, clk_freq=125e6):
    """
    Calculate the integer and fractional dividers for a given target frequency
    and clock frequency (default 125MHz).
    """
    divider = clk_freq / target_freq
    assert 1 <= divider <= 65536
    int_divider = int(divider)
    frac_divider = int((divider - int_divider) * 256)
    return (int_divider, frac_divider)
