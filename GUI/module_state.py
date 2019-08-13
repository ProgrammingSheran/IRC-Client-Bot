'''
--- Avocado (15) --- © Copyright 2019 | All Rights Reserved! ---

This file represents the module state feature.
The appearing window is showing the state of the analyse modules
involved in this project. If there is something wrong with the modules
you can instantly see that in the module state window.
There is a ModuleState class with its functions for checking the
modules in the Modules folder.
There also is an Error_Window class for the appearing error window.
'''

# Importing important modules
from PyQt5.QtCore import pyqtSignal, QThread, QRect
from PyQt5.QtWidgets import *
from PyQt5.Qt import QFrame
import os
import sys

# Class for the ErrorWindow
class Error_Window(QMainWindow):

    # Creating the __init__ method with its thread which will be executed when the program is started
    def __init__(self):
        super().__init__()
        # Creating the Thread, connecting the functions and finally starting the Thread
        self.threader = ModuleState()
        self.threader.complete.connect(self.ModulesComplete)
        self.threader.exist.connect(self.ModulesExist)
        self.threader.ok.connect(self.ModuleOK)
        self.threader.not_ok.connect(self.ModuleNotOK)
        self.threader.start()

        # Calling the main UI
        self.UI()

    def UI(self):

        # Creating labels and UI specific elements
        self.MainLabel = QLabel("Module State", self)
        self.MainLabel.move(120,20)
        self.MainLabel.resize(400,50)
        self.MainLabel.setStyleSheet("font-size: 40px; font-weight: bold; text-decoration: underline;")

        self.line = QFrame(self)
        self.line.setGeometry(QRect(5, 20, 490, 150))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.ModulesField = QTextEdit(self)
        self.ModulesField.move(100,180)
        self.ModulesField.resize(300,310)
        self.ModulesField.setReadOnly(True)

        self.CompleteLabel = QLabel("", self)
        self.CompleteLabel.move(100,100)
        self.CompleteLabel.resize(300,40)
        self.CompleteLabel.setStyleSheet("font-size: 25px; font-style: italic;")

        self.ExistLabel = QLabel("", self)
        self.ExistLabel.move(100,140)
        self.ExistLabel.resize(400,40)
        self.ExistLabel.setStyleSheet("font-size: 25px; font-style: italic;")

        self.setGeometry(200,200,500,510)
        self.setFixedSize(500,510)
        self.show()

    # Creating Thread specific functions for executing
    def ModulesComplete(self, c):
        if str(c) == "Complete":
            try:
                self.CompleteLabel.setText("All modules complete!")
            except:
                self.CompleteLabel.setText("Unknown error!")
        elif str(c) == "Incomplete":
            try:
                self.CompleteLabel.setText("Modules are not complete!")
            except:
                self.CompleteLabel.setText("Unknown error!")

    def ModulesExist(self, module):
        if str(module) == "Exist":
            try:
                self.ExistLabel.setText("Modules in folder EXIST!")
            except:
                self.ExistLabel.setText("Unknown error!")
        elif str(module) == "Don't exist":
            try:
                self.ExistLabel.setText("There is missing one or more modules!")
            except:
                self.ExistLabel.setText("Unknown error!")

    def ModuleOK(self, module):
        try:
            self.ModulesField.setText(self.ModulesField.toPlainText() + str(module)+ "\n")
        except:
            self.ModulesField.setText("Unknown error!")

    def ModuleNotOK(self, module):
        try:
            self.ModulesField.setText(self.ModulesField.toPlainText() + str(module)+ "\n")
        except:
            self.ModulesField.setText("Unknown error!")

# Creating the module state class
class ModuleState(QThread):

    # Creating the signals for transmitting data between this and other classes
    module_error = pyqtSignal(str)
    complete = pyqtSignal(str)
    exist = pyqtSignal(str)
    ok = pyqtSignal(str)
    not_ok = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # Default list of modules which are included by default
        self.modules = ['AnalyseWindow.py', 'check_amazon.py', 'check_animals.py', 'check_companies.py', 'check_email.py', 'check_google.py',
                        'check_greetings.py', 'check_link.py', 'check_magazines.py', 'check_math.py', 'check_misspelled.py',
                        'check_movies.py', 'check_people.py', 'check_pexist.py', 'check_questions.py', 'check_socialm.py',
                        'check_trademarks.py', 'check_wikipedia.py', 'check_youtube.py', 'get_message.py','link_warn.py','send_email.py',
                        'send_pre.py']

    # Function for listing the modules
    def list_modules(self):
        try:
            Modules_List = [str(module) for module in os.listdir("C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\")]
            Modules_List.remove("__pycache__")
            Modules_List.remove("animals.json")
            return Modules_List
        except:
            self.module_error.emit("Module Error occurred!")

    # Checking if all modules are complete
    def check_complete(self):

        if self.list_modules() == self.modules:
            self.complete.emit("Complete")
        else:
            self.complete.emit("Incomplete")

    # Checking if the modules exist
    def check_exist(self):
        self.mpath = "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\"

        for module in self.modules:
            if os.path.exists(self.mpath + module):
                self.exist.emit("Exist")
            else:
                self.exist.emit("Don't exist")

        return True

    # Final check for the modules
    def check_modules(self):
        for module in self.modules:
            if os.path.exists(self.mpath + module):
                self.ok.emit(module + " --> " + "OK!")
            else:
                self.not_ok.emit(module + " --> " + "Not OK!")

    # Overriding the run class of the QThread class. Will be executed when calling the class
    def run(self):
        #self.list_modules()
        self.check_complete()
        self.check_exist()
        self.check_modules()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Error_Window()
    sys.exit(app.exec())
