#!/usr/bin/env python
from __future__ import division, print_function

import sched
import sys
import time
from timeit import default_timer
try:
    from Tkinter import Tk
except ImportError: # Python 3
    from tkinter import Tk

def timer():
    return int(default_timer() * 1 + .5)

def tick(interval, function, *args):
    s.enter(interval - timer() % interval, 10, tick, (interval, function, *args))
    function(*args) # assume it doesn't block

def bpm(milliseconds):
    """Beats per minute."""
    if milliseconds != 0:
        return milliseconds
    else:
        return 0

def print_tempo(last=[timer()], total=[0], count=[0]):
    now = timer()
    elapsed = now - last[0]
    total[0] += elapsed
    count[0] += 1
    average = total[0] / count[0]
    print("{:.10f} BPS, average: {:.10f} BPM, now {}"
          .format(bpm(elapsed), bpm(average), now),
          end='\n', file=sys.stderr)
    last[0] = now

interval = 0.25
s = sched.scheduler(time.time, time.sleep)
s.enter(interval - timer() % interval, 10, tick, (interval, print_tempo))
s.run()
