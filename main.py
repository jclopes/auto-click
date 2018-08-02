import sys
import time
import cv2 as cv
import numpy as np
import pyautogui

def findButton(img):
  img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  template = cv.imread('template.png', 0)
  w, h = template.shape[::-1]

  res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
  min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

  if max_val < 0.8:
    return None
  return max_loc

def takeShot():
  screenshot = pyautogui.screenshot()
  screenshot = cv.cvtColor(np.array(screenshot), cv.COLOR_RGB2BGR)
  return screenshot

def main():
  is_retina = True
  screenshot = takeShot()
  buttonPos = findButton(screenshot)

  while (buttonPos == None):
    time.sleep(2)
    screenshot = takeShot()
    buttonPos = findButton(screenshot)

  xx, yy = buttonPos
  if is_retina:
    xx /= 2
    yy /= 2
  pyautogui.click(xx,yy)

if __name__ == '__main__':
  sys.exit(main())
