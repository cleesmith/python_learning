#!/usr/bin/python
import signal
import io
import socket
import numpy as np
import picamera
import picamera.array
import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
LOG = logging.getLogger("capture_motion")

def signal_term_handler(signal, frame):
  LOG.info('shutting down ...')
  # this raises SystemExit(0) which fires all "try...finally" blocks:
  sys.exit(0)

# this is useful when this program is started at boot via init.d
# or an upstart script, so it can be killed: i.e. kill some_pid:
signal.signal(signal.SIGTERM, signal_term_handler)

HOST = '192.168.0.2'
PORT = 9876
HOST_PORT = (HOST,PORT)
BUFSIZE = 4096

minimum_still_interval = 5
motion_detected = False
last_still_capture_time = datetime.datetime.now()

# The 'analyse' method gets called on every frame processed while picamera
# is recording h264 video.
# It gets an array (see: "a") of motion vectors from the GPU.
class DetectMotion(picamera.array.PiMotionAnalysis):
  def analyse(self, a):
    global minimum_still_interval, motion_detected, last_still_capture_time
    if datetime.datetime.now() > last_still_capture_time + \
        datetime.timedelta(seconds=minimum_still_interval):
      a = np.sqrt(
        np.square(a['x'].astype(np.float)) +
        np.square(a['y'].astype(np.float))
      ).clip(0, 255).astype(np.uint8)
      # experiment with the following "if" as it may be too sensitive ???
      # if there're more than 10 vectors with a magnitude greater
      # than 60, then motion was detected:
      if (a > 60).sum() > 10:
        LOG.info('motion detected at: %s' % datetime.datetime.now().strftime('%Y-%m-%dT%H.%M.%S.%f'))
        motion_detected = True

camera = picamera.PiCamera()
with DetectMotion(camera) as output:
  try:
    camera.resolution = (640, 480)
    camera.framerate= 10
    # record video to nowhere, as we are just trying to capture images:
    camera.start_recording('/dev/null', format='h264', motion_output=output)
    while True:
      while not motion_detected:
        LOG.info('waiting for motion...')
        camera.wait_recording(1)

      LOG.info('stop recording and capture an image...')
      camera.stop_recording()
      motion_detected = False

      # replace the following code that saves the image to a file with:
      # 1. scp or somehow copy image to another computer,
      #    such as gdrive, ftp, or a shared folder
      # 2. use tcp to stream the image to a a web browser via a web server,
      #    such as nginx, python -m SimpleHTTPServer, gstreamer, or ???
      # just avoid saving the file to disk ... why?
      # a raspberry pi is limited to a microSD for storage, so the
      # repetition of adding/deleting images will wear it out

      # filename = '/home/pi/picamera_quick_start/img_' + \
      #   datetime.datetime.now().strftime('%Y-%m-%dT%H.%M.%S.%f') + '.jpg'
      # camera.capture(filename, format='jpeg', use_video_port=True)
      # LOG.info('image captured to file: %s' % filename)

      stream = io.BytesIO()
      camera.capture(stream, format='jpeg', use_video_port=True)
      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.connect(HOST_PORT)
      connection = client.makefile('wb')
      # rewind the stream and send the image data:
      stream.seek(0)
      connection.write(stream.read())
      connection.close()
      client.close()
      LOG.info('image captured/sent via stream')
      # Reset the stream for the next capture
      stream.seek(0)
      stream.truncate()

      # record video to nowhere, as we are just trying to capture images:
      camera.start_recording('/dev/null', format='h264', motion_output=output)
  except KeyboardInterrupt as e:
    LOG.info("\nreceived KeyboardInterrupt via Ctrl-C")
    pass
  finally:
    camera.close()
    LOG.info("\ncamera turned off!")
    LOG.info("detect motion has ended.\n")
