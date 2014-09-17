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

motion_dtype = np.dtype([
  (native_str('x'), np.int8),
  (native_str('y'), np.int8),
  (native_str('sad'), np.uint16)
])

class MyOutput(object):
  def __init__(self, camera):
    self.camera = camera
    self.cols = None
    self.rows = None

  def write(self, b):
    if self.cols is None:
      width, height = self.camera.resolution
      self.cols = ((width + 15) // 16) + 1
      self.rows = (height + 15) // 16
    self.analyse(np.frombuffer(b, dtype=motion_dtype).reshape((self.rows, self.cols)))
    return len(b)

  def analyse(self, a):
    print('a=',a)

with picamera.PiCamera() as camera:
  camera.resolution = (640, 480)
  camera.start_recording('/dev/null', 'h264', motion_output=MyOutput(camera))
  camera.wait_recording(10)
