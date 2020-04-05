from threading import Thread

import numpy
import numpy as np
import cv2
import cv2.cv2
import time

time2 = time.time()

from PIL import ImageGrab, Image

fps = 30

seconds = 10

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (1920, 1080))

img = Image.new("RGB", (1920, 1080))
a = [img]

import sched, time
s = sched.scheduler(time.time, time.sleep)

global_time = time.time()


starttime=time.time()
for i in range(fps*seconds):
  img2 = ImageGrab.grab(include_layered_windows=True)
  a.append(img2)
  print(time.asctime(time.gmtime(time.time())))

  time.sleep(1/fps - ((time.time() - starttime) % 1/fps))
#
#
# def do_something(sc: sched.scheduler, i):
#     # if i>fps*seconds:
#     #     return
#     # Thread(target=lambda: sc.enterabs(global_time+(i/fps), 10, do_something, (s, i+1))).start()
# s.enterabs(global_time+(0/fps), 10, do_something, (s, 0))
# s.run()
# for i in range(fps * seconds):
#     time1 = time.time()
#     m = (time1 - time2)
#     time2 = time.time()
#     c = 1/fps
#     f = 0 - (m - c)
#     # print(m, time1, time2, f, c)
#
#     img2 = ImageGrab.grab(include_layered_windows=True)
#     if f > 0:
#         # write the flipped frame
#         a.append(img2)
#
#         time.sleep((f/fps))
#     else:
#         a.append(a[-1])
#         time2 = time.time()
#
#     print(i, time.asctime(time.gmtime(time.time())), f)
#
#     # cv2.imshow('frame',frame)
#     # if cv2.waitKey(1) & 0xFF == ord('q'):
#     #     break
#
#
for img in a[1:]:
    frame = numpy.array(img)
    out.write(frame)


# Release everything if job is finished
# cap.release()
out.release()
cv2.destroyAllWindows()
