import pyautogui
import win32api
import win32con
import keyboard
import random
import time

# https://gameforge.com/en-US/littlegames/magic-piano-tiles/#  #link of game

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(random.randint(.015, .03))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


quit_key = 'q'
positions = [(400, 500), (490, 500), (580, 500), (670, 500)]

input('When load the page, press enter...')
time.sleep(2)

while not keyboard.is_pressed(quit_key):
    try:
        for x, y in positions:
            if not pyautogui.pixel(x, y)[2]:  # if the pixel was black
                click(x, y)

    except Exception:
        pass
