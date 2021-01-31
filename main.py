import signal
import os
import sys
import time
import cv2 as cv
import numpy as np
import pyautogui


def midPoint(template, px, py):
  xx = px + (len(template[0]) / 2)
  yy = py + (len(template) / 2)
  return (xx, yy)

def scalePoint(point, factor):
  x, y = point
  return (int(x*factor), int(y*factor))

def findButton(img, templates):
  """Matches a template against an image an returns the
  center point where the image was found.
  Returns None if there is no match.
  """
  # scale down the images by a factor of 4. This will help with performance.
  img_r = cv.resize(img, (0,0), fx=0.25, fy=0.25)
  
  for template in templates:
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_r, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if max_val > 0.8:
      px, py = max_loc
      mp = midPoint(template, px, py)
      # need to revert the downscaling.
      return scalePoint(mp, 4)
  return None


def takeShot():
  """Takes a Graysacle screenshot."""
  screenshot = pyautogui.screenshot("capture.png")
  screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_BGR2GRAY)
  return screenshot


def terminate():
  print("\nShutting down...")
  try:
    os.remove("capture.png")
  except OSError:
    pass
  print("Terminated.")


def main():
  is_retina = False
  for i in sys.argv:
    if i == 'retina':
      is_retina = True
  # TODO: check if the template files exist
  templates = list()
  # scale down the images by a factor of 4. This will help with performance.
  templates.append(cv.resize(cv.imread('template01.png', 0), (0,0), fx=0.25, fy=0.25))
  templates.append(cv.resize(cv.imread('template02.png', 0), (0,0), fx=0.25, fy=0.25))

  while True:
    match_t = None
    while (match_t is None):
      time.sleep(1.5)
      screenshot = takeShot()
      match_t = findButton(screenshot, templates)

    if (is_retina):
      # retina screens have double pixel dencity
      match_t = scalePoint(match_t, 0.5)
    xx, yy = match_t

    pyautogui.click(xx,yy)
    time.sleep(0.5)
    pyautogui.moveTo(20, 20)


def signal_handler(signal, frame):
  terminate()
  sys.exit(0)


if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal_handler)
  print('Press Ctrl+C to exit')
  sys.exit(main())
