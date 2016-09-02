#! /usr/bin/python3

"""Script moves the mouse cursor on the screen. Movement is repeated using an
infinite loop until a user terminates the script with Ctrl + c

required packages:
Pillow
Xlib
pyautogui
"""
import time
import pyautogui

# Disabling FAILSAFE
# Check pyautogui documentation for more info
pyautogui.FAILSAFE = False


def move_the_mouse():
    """Function moves the cursor in the upper right corner and then 100 px
    to the right side"""
    # Get the screen size
    screen_width, screen_height = pyautogui.size()
    # Move the mouse in a rectange shape
    pyautogui.moveTo(60, 60, duration=0.50)
    pyautogui.moveTo(screen_width - 60, 60, duration=0.50)
    pyautogui.moveTo(screen_width - 60, screen_height - 60, duration=0.50)
    pyautogui.moveTo(60, screen_height - 60, duration=0.50)


def sleep(seconds):
    """Function that stops the process for n seconds"""
    time.sleep(seconds)


def main():
    """Calling the move_the_mouse and sleep functions in an infinite loop"""
    print("Mouse mover")
    print("Press Ctrl + c to terminate the script.")
    try:
        while True:
            move_the_mouse()
            sleep(2)

    except KeyboardInterrupt:
        print("Finished.")

main()
