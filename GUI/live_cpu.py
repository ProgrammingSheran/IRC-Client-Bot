'''
--- Avocado (15) --- © Copyright 2019 | All Rights Reserved! ---

This file represents the CPU state included in the GUI
This is a live CPU state showing up in the GUI in form of
a so called ProgressBar.
There's a Live_CPU class which is inheriting from QThread class.
There a several error and critical CPU catchings built-in.
So in case of an error or critical CPU states the GUI will warn you
or exit exit if the CPU exceeds a certain value!
'''

# Importing important modules
from PyQt5.QtCore import pyqtSignal, QThread
import psutil
from time import sleep
import sys

class Live_CPU(QThread):

    # Setting up variables for the CPU
    cpu_state = pyqtSignal(int)
    error = pyqtSignal(str)
    warning = pyqtSignal(str)

    # Setting up (overriding) the run function of the QThread
    def run(self):
        # Starting a loop for always measuring the CPU and transmitting
        while True:
            try:
                # Setting up variables for the CPU
                cpu = psutil.cpu_percent()
                self.cpu_state.emit(cpu)

                # Checking for values and raising errors when needed
                if int(cpu) < 80:
                    self.warning.emit("CPU:")
                elif int(cpu) > 80 and int(cpu) < 90:
                    self.warning.emit("CPU WARNING!")
                elif int(cpu) > 90 and int(cpu) < 95:
                    self.warning.emit("CRITICAL CPU!")
                elif int(cpu) > 95:
                    self.close()

                sleep(1)
            except:
                self.error.emit("Error")

if __name__ == "__main__":
    Live_CPU()
