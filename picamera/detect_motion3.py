from __future__ import (
    unicode_literals,
    absolute_import,
    print_function,
    division,
)

import numpy as np
import picamera
import picamera.array

native_str = str
str = type('')

class MotionAnalyser(picamera.array.PiMotionAnalysis):
  def analyse(self, a):
    a = np.sqrt(
      np.square(a['x'].astype(np.float)) +
      np.square(a['y'].astype(np.float))
    ).clip(0, 255).astype(np.uint8)
    h, edges = np.histogram(a, bins=10, range=(0, 255))
    h = h / (a.shape[0] * a.shape[1] / 6)
    print(' '.join('%6s' % ('#'*n) for n in h))

with picamera.PiCamera() as camera:
  camera.resolution = (640, 480)
  with MotionAnalyser(camera) as output:
    camera.start_recording('mo3.h264', 'h264', motion_output=output)
    camera.wait_recording(10)
