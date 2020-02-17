import signal
import os
import sys
import time
import cv2 as cv
import numpy as np
import pyautogui


def midPoint(template, px, py):
  is_retina = True
  xx = px + (len(template[0]) / 2)
  yy = py + (len(template) / 2)
  # retina display have double pixels density
  if(is_retina):
    xx /= 2
    yy /= 2
  return (xx, yy)


def findButton(img, templates):
  img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  for template in templates:
    w, h = template.shape[::-1]

    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if max_val > 0.8:
      px, py = max_loc
      return midPoint(template, px, py)
  return None


def takeShot():
  screenshot = pyautogui.screenshot("capture.png")
  screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
  return screenshot


def terminate():
  print("\nShutting down...")
  try:
    os.remove("capture.png")
  except OSError:
    pass
  print("Terminated.")


def main():
  templates = list()
  templates.append(cv.imread('template01.png', 0))
  templates.append(cv.imread('template02.png', 0))

  while True:
    match_t = None
    while (match_t is None):
      time.sleep(1.5)
      screenshot = takeShot()
      match_t = findButton(screenshot, templates)
    xx, yy = match_t
    pyautogui.click(xx,yy)


def signal_handler(signal, frame):
  terminate()
  sys.exit(0)


if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal_handler)
  print('Press Ctrl+C to exit')
  sys.exit(main())
