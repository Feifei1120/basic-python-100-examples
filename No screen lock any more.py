import pyautogui #Terminal里安装pip install pyautogui
import random
import time

while True:
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    pyautogui.moveRel(x,y)
    time.sleep(2)


