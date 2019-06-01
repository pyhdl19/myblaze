#!/usr/bin/env  python
# top_sample_veri1.py

# insert pythonpath  ../../rtl
import os
import sys
sys.path.insert(0, os.path.abspath("../../rtl"))

from myhdl import Signal, intbv, toVerilog
from local_mod_numpy import log2

from top import SysTop

if __name__ == '__main__':
    txd_line = Signal(False)
    rxd_line = Signal(False)
    txd_line2 = Signal(False)
    rxd_line2 = Signal(False)
    leds = Signal(intbv(0)[8:])
    reset = Signal(False)
    clock = Signal(False)
    size = int(log2(int(sys.argv[1]))) if len(sys.argv) > 1 else 4
    print 'size=%s' % size
    #toVHDL(uart_test_top, txd_line, rxd_line, leds, reset, clock)
    toVerilog(SysTop, txd_line, rxd_line, txd_line2, rxd_line2, leds, reset,
            clock, size=size, DEBUG=False)
