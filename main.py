import signal
import sys
import time
import cv2 as cv
import numpy as np
import pyautogui


def findButton(img, template):
  img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  w, h = template.shape[::-1]

  res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
  min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

  if max_val < 0.9:
    return None
  return max_loc


def takeShot():
  screenshot = pyautogui.screenshot()
  screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
  return screenshot


def main():
  is_retina = True
  template = cv.imread('template.png', 0)
  buttonPos = None

  while True:
    while (buttonPos == None):
      time.sleep(1.5)
      screenshot = takeShot()
      buttonPos = findButton(screenshot, template)

    xx, yy = buttonPos
    buttonPos = None

    # click on the midle of the template
    xx += len(template[0]) / 2
    yy += len(template) / 2

    # retina display have double pixels density
    if is_retina:
      xx /= 2
      yy /= 2
    pyautogui.click(xx,yy)


def signal_handler(signal, frame):
  print('\nTerminating...\n')
  sys.exit(0)


if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal_handler)
  print('Press Ctrl+C to exit')
  sys.exit(main())
