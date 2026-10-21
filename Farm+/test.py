import pyautogui as py
from time import sleep

sleep(1)
py.moveTo(x=1460, y=210)
sleep(1)
for n in range(12):
    py.scroll(-100)