import pyautogui

from subprocess import call
call(["screencapture", "screenshot.jpg"])


im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('my_screenshot.png')
from PIL import Image

img = Image.open('my_screenshot.png')
img.show()
# open(im1)