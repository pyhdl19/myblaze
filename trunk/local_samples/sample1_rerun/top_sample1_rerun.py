#!/usr/bin/env  python
# top_sample1_rerun.py

# insert pythonpath  ../../rtl
import os
import sys
sys.path.insert(0, os.path.abspath("../../rtl"))

import myhdl

import top

if __name__ == '__main__':
    top.local_mod_no_prepare = True # add this to avoid composing romN.vmem from rom.vmem
    tb = myhdl.traceSignals(top.TopBench)
    myhdl.Simulation(tb).run()
