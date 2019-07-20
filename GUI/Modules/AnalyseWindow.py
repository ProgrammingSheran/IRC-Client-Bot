from PyQt5.QtWidgets import *
import sys
from PyQt5.Qt import *
from check_amazon import *
from check_animals import *
import subprocess

class Anim(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_amazon.py"])

class AnalyseWindow(QWidget):

    def __init__(self):
        super().__init__()
        # Stuff to initialize ...
        # Calling the UI
        self.UI()

    def UI(self):

        self.mainHeading = QLabel("Analyse Operations", self)
        self.mainHeading.move(120,20)
        self.mainHeading.resize(400,40)
        self.mainHeading.setStyleSheet("font-size: 40px; font-weight: bold;")

        self.line = QFrame(self)
        self.line.setGeometry(QRect(1, 20, 600, 110))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.button1 = QPushButton("Amazon", self)
        self.button2 = QPushButton("Animals", self)
        self.button3 = QPushButton("Companies", self)
        self.button4 = QPushButton("E-Mail", self)
        self.button5 = QPushButton("Google", self)
        self.button6 = QPushButton("Greetings", self)
        self.button7 = QPushButton("Link", self)
        self.button8 = QPushButton("Magazines", self)
        self.button9 = QPushButton("Math", self)
        self.button10 = QPushButton("Misspelled", self)
        self.button11 = QPushButton("Movies", self)
        self.button12 = QPushButton("People", self)
        self.button13 = QPushButton("Page-Exist", self)
        self.button14 = QPushButton("Questions", self)
        self.button15 = QPushButton("Social-Media", self)
        self.button16 = QPushButton("Trademarks", self)
        self.button17 = QPushButton("Wikipedia", self)
        self.button18 = QPushButton("YouTube", self)
        self.button19 = QPushButton("Link-Warn", self)
        self.button20 = QPushButton("Send-E-Mail", self)
        self.button21 = QPushButton("Send-Pre-Answer", self)

        # First row
        self.button1.move(50,150)
        self.button1.resize(100,50)
        self.button2.move(50, 220)
        self.button2.resize(100,50)
        self.button3.move(50, 290)
        self.button3.resize(100,50)
        self.button4.move(50, 360)
        self.button4.resize(100,50)
        self.button5.move(50, 430)
        self.button5.resize(100,50)

        # Second row
        self.button6.move(170, 150)
        self.button6.resize(100, 50)
        self.button7.move(170, 220)
        self.button7.resize(100, 50)
        self.button8.move(170, 290)
        self.button8.resize(100, 50)
        self.button9.move(170, 360)
        self.button9.resize(100, 50)
        self.button10.move(170, 430)
        self.button10.resize(100, 50)

        # Third row
        self.button11.move(290, 150)
        self.button11.resize(100, 50)
        self.button12.move(290, 220)
        self.button12.resize(100, 50)
        self.button13.move(290, 290)
        self.button13.resize(100, 50)
        self.button14.move(290, 360)
        self.button14.resize(100, 50)
        self.button15.move(290, 430)
        self.button15.resize(100, 50)

        # Fourth row
        self.button16.move(410, 150)
        self.button16.resize(100, 50)
        self.button17.move(410, 220)
        self.button17.resize(100, 50)
        self.button18.move(410, 290)
        self.button18.resize(100, 50)
        self.button19.move(410, 360)
        self.button19.resize(100, 50)
        self.button20.move(410, 430)
        self.button20.resize(100, 50)
        self.button21.move(230,500)
        self.button21.resize(100,50)

        # Button functions TODO Set up the functions

        self.button1.clicked.connect(self.Amazon)
        self.button2.clicked.connect(self.Animals)

        self.setGeometry(200, 200, 600, 600)
        self.setFixedSize(600, 600)
        self.show()

    # FUNCTIONS

    def Amazon(self):
        self.th = Anim()
        self.th.start()
        #self.CheckA = CheckAmazon()
        #pass


    def Animals(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_animals.py"])
        #self.CheckAN = CheckAnimals()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AnalyseWindow()
    sys.exit(app.exec())