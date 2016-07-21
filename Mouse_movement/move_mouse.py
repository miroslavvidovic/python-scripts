#! /usr/bin/python3

"""Script moves the mouse cursor on the screen. Movement is repeated using an
infinite loop until a user terminates the script with Ctrl + c

required packages:
Pillow
Xlib
pyautogui
"""
import pyautogui, time

# Disabling FAILSAFE
# Check pyautogui documentation for more info
pyautogui.FAILSAFE = False


def move_the_mouse():
    """Function moves the cursor in the upper right corner and then 100 px
    to the right side"""
    pyautogui.moveTo(10, 10, duration=0.50)
    pyautogui.moveTo(100, 10, duration=0.50)


def sleep(seconds):
    """Function that stops the process for n seconds"""
    time.sleep(seconds)


def main():
    """Calling the move_the_mouse and sleep functions in an infinite loop"""
    print("Press Ctrl + c to terminate the script.")
    try:
        while True:
            move_the_mouse()
            sleep(3)

    except KeyboardInterrupt:
        print("Finished.")

main()
