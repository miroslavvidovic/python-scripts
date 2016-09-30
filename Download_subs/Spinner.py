"""
Spinner.py

Spinner animation

"""

import sys
import time
import threading

class Spinner:
    """
    Spinner running in a separate thread

    """

    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        """
        Static method for the cursor animation

        """
        while 1:
            for cursor in '|/-\\':
                yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay):
            self.delay = delay

    def spinner_task(self):
        """
        Write the cursor to the screen and create a feeling of a loading animation

        """
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def start(self):
        """
        Start the spinner

        """
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        """
        Stop the spinner

        """
        self.busy = False
        time.sleep(self.delay)
