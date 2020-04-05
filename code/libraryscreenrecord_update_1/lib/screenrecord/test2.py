import sys
import time
import timeit


def timer():
    return int(timeit.default_timer() * 1 + .5)


def bpm(milliseconds):
    """Beats per minute."""
    if milliseconds != 0:
        return milliseconds
    else:
        return 0


# noinspection PyDefaultArgument
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

starttime=time.time()
while True:
  print_tempo()
  time.sleep(0.1 - ((time.time() - starttime) % 0.1))
