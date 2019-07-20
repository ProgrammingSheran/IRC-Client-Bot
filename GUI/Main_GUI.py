'''
--- Simon Meins (15) --- © Copyright 2019 | All Rights Reserved! ---

This file represents the whole GUI (Graphical User Interface) of the
IRC-Client-Bot-Project. Everything that has to do with design is included
in this file.
Architecture:

This file has access to different classes of other files. These files all include
classes with their respective functionality. All of the files are multi threaded.
That means they'll be executed in background if a certain action is triggered from
the GUI. All of the features of the analyse implementations are described in the enormous
schedule.
'''

# Importing important module for the GUI and functions
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
import socket
from live_cpu import *
from module_state import *
#from main_socket import *
from IRC.main_socket import MainIRC
import subprocess

class OpenAmazon(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_amazon.py"])

class OpenAnimals(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_animals.py"])

class OpenCompanies(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_companies.py"])

class OpenEMailCheck(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_email.py"])

class OpenGoogle(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_google.py"])

class OpenGreetings(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_greetings.py"])

class OpenLink(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_link.py"])

class OpenMagazines(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_magazines.py"])

class OpenMath(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_math.py"])

class OpenMisspelled(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_misspelled.py"])

class OpenMovies(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_movies.py"])

class OpenPeople(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_people.py"])

class OpenPageExist(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_pexist.py"])

class OpenCheckQuestions(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_questions.py"])

class OpenCheckSocialMedia(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_socialm.py"])

class OpenCheckTradeMarks(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_trademarks.py"])

class OpenWikipedia(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_wikipedia.py"])

class OpenYouTube(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\check_youtube.py"])

class OpenLinkWarn(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\link_warn.py"])

class OpenEMailSend(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\send_email.py"])

class OpenSendPreDefinedAnswer(QThread):
    def run(self):
        subprocess.call(["python", "C:\\Python37\\PyCharm\\IRC-Project\\GUI\\Modules\\send_pre.py"])

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
        self.button3.clicked.connect(self.Companies)
        self.button4.clicked.connect(self.EMailCheck)
        self.button5.clicked.connect(self.Google)
        self.button6.clicked.connect(self.Greetings)
        self.button7.clicked.connect(self.LinkCheck)
        self.button8.clicked.connect(self.Magazines)
        self.button9.clicked.connect(self.Math)
        self.button10.clicked.connect(self.Misspelled)
        self.button11.clicked.connect(self.Movies)
        self.button12.clicked.connect(self.People)
        self.button13.clicked.connect(self.PageExist)
        self.button14.clicked.connect(self.Questions)
        self.button15.clicked.connect(self.SocialMedia)
        self.button16.clicked.connect(self.TradeMarks)
        self.button17.clicked.connect(self.Wikipedia)
        self.button18.clicked.connect(self.YouTube)
        self.button19.clicked.connect(self.LinkWarn)
        self.button20.clicked.connect(self.SendEMail)
        self.button21.clicked.connect(self.PreAnswer)

        self.setGeometry(200, 200, 600, 600)
        self.setFixedSize(600, 600)
        self.show()

    # FUNCTIONS

    def Amazon(self):
        self.OpenAmazon = OpenAmazon()
        self.OpenAmazon.start()

    def Animals(self):
        self.OpenAnimals = OpenAnimals()
        self.OpenAnimals.start()

    def Companies(self):
        self.OpenCompanies = OpenCompanies()
        self.OpenCompanies.start()

    def EMailCheck(self):
        self.OpenEmailCheck = OpenEMailCheck()
        self.OpenEmailCheck.start()

    def Google(self):
        self.OpenGoogle = OpenGoogle()
        self.OpenGoogle.start()

    def Greetings(self):
        self.OpenGreetings = OpenGreetings()
        self.OpenGreetings.start()

    def LinkCheck(self):
        self.OpenLink = OpenLink()
        self.OpenLink.start()

    def Magazines(self):
        self.OpenMagazines = OpenMagazines()
        self.OpenMagazines.start()

    def Math(self):
        self.OpenMath = OpenMath()
        self.OpenMath.start()

    def Misspelled(self):
        self.OpenMisspelled = OpenMisspelled()
        self.OpenMisspelled.start()

    def Movies(self):
        self.OpenMovies = OpenMovies()
        self.OpenMovies.start()

    def People(self):
        self.OpenPeople = OpenPeople()
        self.OpenPeople.start()

    def PageExist(self):
        self.OpenPageExist = OpenPageExist()
        self.OpenPageExist.start()

    def Questions(self):
        self.OpenQuestions = OpenCheckQuestions()
        self.OpenQuestions.start()

    def SocialMedia(self):
        self.OpenSocialMedia = OpenCheckSocialMedia()
        self.OpenSocialMedia.start()

    def TradeMarks(self):
        self.OpenTradeMarks = OpenCheckTradeMarks()
        self.OpenTradeMarks.start()

    def Wikipedia(self):
        self.OpenWikipedia = OpenWikipedia()
        self.OpenWikipedia.start()

    def YouTube(self):
        self.OPenYouTube = OpenYouTube()
        self.OPenYouTube.start()

    def LinkWarn(self):
        self.OpenLinkWarn = OpenLinkWarn()
        self.OpenLinkWarn.start()

    def SendEMail(self):
        self.OpenSendEMail = OpenEMailSend()
        self.OpenSendEMail.start()

    def PreAnswer(self):
        self.OpenPreAnswer = OpenSendPreDefinedAnswer()
        self.OpenPreAnswer.start()

# Private Message Dialog - not used anymore! --> New function implemented
class PrivateMSG(QMainWindow):

    def __init__(self):
        super().__init__()
        self.UI()

        self.PrivateMSGThread = PrivateMSGThread(self.PrivateMSGMessage.toPlainText(), self.PrivatMSGReceiver.text())

        self.PrivateMSGThread.send.connect(self.CheckSend)
        self.PrivateMSGThread.conn.connect(self.CheckConnection)
        self.PrivateMSGThread.log_in.connect(self.CheckLOG_IN)
        self.PrivateMSGThread.nick.connect(self.CheckNICK)

        self.PrivateMSGThread.start()

    def UI(self):

        self.PrivatMSGReceiver = QLineEdit(self)
        self.PrivatMSGReceiver.move(100,30)
        self.PrivatMSGReceiver.resize(200,30)

        self.PrivateMSGMessage = QTextEdit(self)
        self.PrivateMSGMessage.move(50,80)
        self.PrivateMSGMessage.resize(300,300)

        self.MessageLabel = QLabel("", self)
        self.MessageLabel.move(400, 50)
        self.MessageLabel.resize(300,100)
        self.MessageLabel.setStyleSheet("font-size: 15px;")

        self.MessageSendLabel = QLabel("", self)
        self.MessageSendLabel.move(400, 200)
        self.MessageSendLabel.resize(300,100)
        self.MessageSendLabel.setStyleSheet("font-size: 15px;")

        self.SendMessage = QPushButton("Send", self)
        self.SendMessage.move(100,400)
        self.SendMessage.resize(100,80)
        self.SendMessage.clicked.connect(self.StartingMessageThread)

        self.setGeometry(200,200,600,600)
        self.show()

    def CheckSend(self, value):
        if int(value) == 1:
            self.MessageSendLabel.setText("Message send successfully!")
        else:
            self.MessageSendLabel.setText("Error!")

    def CheckConnection(self, value):
        if str(value) == "Connection established":
            self.MessageLabel.setText(self.MessageLabel.text() + "Connection established"+ "\n")
        else:
            self.MessageLabel.setText(self.MessageLabel.text() + "Error!" + "\n")

    def CheckLOG_IN(self, value):
        if str(value) == "Success":
            self.MessageLabel.setText(self.MessageLabel.text() + "Log in successfully!"+ "\n")
        else:
            self.MessageLabel.setText(self.MessageLabel.text() + "Error!" + "\n")

    def CheckNICK(self, value):
        if str(value) == "Success":
            self.MessageLabel.setText(self.MessageLabel.text() + "Nick successfully set!" + "\n")
        else:
            self.MessageLabel.setText(self.MessageLabel.text() + "Error!" + "\n")

    def StartingMessageThread(self):
        self.PrivateMSGThread.send_private_message(self.PrivateMSGMessage.toPlainText(), self.PrivatMSGReceiver.text())

# Creating the Main Class of the Window --> MainWindow
# This class includes all things that have to do with design
# Inheriting from QMainWindow
class MainWindow(QMainWindow):

    # Creating the __init__ method --> Executed when running the GUI
    # When running SOCKET Thread is executed for connecting to the server and receiving the messages
    # By default server is connecting to a test channel (this can be changed within the settings)
    def __init__(self):
        super().__init__()
        # TODO Creating the SOCKET Thread for connecting to the server and channel
        # TODO Starting the Thread

        # Setting up the CPU Thread
        self.CPUThread = Live_CPU()
        self.CPUThread.cpu_state.connect(self.SetCPU)
        self.CPUThread.error.connect(self.CPUError)
        self.CPUThread.warning.connect(self.CPUWarning)
        self.CPUThread.start()

        # Connecting to the Main Method with all methods which are executed when triggering an action

        self.MainGUI()

        self.Main_Socket = MainIRC("SIMONINTHEHOUSE", "irc.freenode.net", "#testit")
        self.Main_Socket.conn.connect(self.CheckConnection)
        #self.Main_Socket.send.connect(self.CheckSend)
        self.Main_Socket.sent_message.connect(self.SetSentMessage)
        self.Main_Socket.received_message.connect(self.SetReceivedMessage)
        self.Main_Socket.log_in.connect(self.CheckLOG_IN)
        self.Main_Socket.nick.connect(self.CheckNICK)
        self.Main_Socket.join.connect(self.CheckJOIN)
        self.Main_Socket.joined.connect(self.JoinedPerson)
        self.Main_Socket.quitted.connect(self.QuittedPerson)
        self.Main_Socket.private_message.connect(self.SetPrivateMessage)
        self.Main_Socket.away_emitter.connect(self.Away)
        self.Main_Socket.back_emitter.connect(self.Back)
        self.Main_Socket.part_leave_emitter.connect(self.Part)
        self.Main_Socket.topic_emitter.connect(self.Topic)
        self.Main_Socket.whois_emitter.connect(self.Whois)
        self.Main_Socket.start()


    def MainGUI(self):

        # Defining actions for the Menu Bar Items
        # File
        self.SaveMessages = QAction(QIcon("Icons\\Save.ico"), "Save Messages", self)
        self.Exit = QAction("Exit", self)
        self.Settings = QAction(QIcon("Icons\\Settings.ico"), "Settings", self)

        # IRC
        self.about = QAction(QIcon("Icons\\About.ico"), "About IRC", self)
        self.join_channel = QAction("Join Channel", self)
        self.change_nick = QAction("Change Nick-Name", self)

        # Setting shortcuts for QActions
        # File
        self.SaveMessages.setShortcut("Ctrl+S")
        self.Exit.setShortcut("Ctrl+E")
        self.Settings.setShortcut("Ctrl+Alt+S")

        # Adding the Menu Bar and Adding registers
        # File Menu
        self.menubar = self.menuBar()
        file = self.menubar.addMenu("&File")
        file.addAction(self.SaveMessages)
        file.addAction(self.Settings)
        file.addAction(self.Exit)

        # IRC Menu
        irc = self.menubar.addMenu("&IRC")
        irc.addAction(self.about)
        irc.addAction(self.join_channel)
        irc.addAction(self.change_nick)

        # Setting up the line which divides the window in two sections
        self.line = QFrame(self)
        self.line.setGeometry(QRect(280, 20, 20, 1920))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        # Setting up the second line for dividing
        self.line2 = QFrame(self)
        self.line2.setGeometry(QRect(1220, 20, 20, 1920))
        self.line2.setFrameShape(QFrame.VLine)
        self.line2.setFrameShadow(QFrame.Sunken)

        # Setting up third line for dividing
        self.line3 = QFrame(self)
        self.line3.setGeometry(QRect(1, 20, 285, 150))
        self.line3.setFrameShape(QFrame.HLine)
        self.line3.setFrameShadow(QFrame.Sunken)

        # Setting up fourth line for dividing
        self.line4 = QFrame(self)
        self.line4.setGeometry(QRect(1230, 20, 285, 150))
        self.line4.setFrameShape(QFrame.HLine)
        self.line4.setFrameShadow(QFrame.Sunken)

        # Setting up the main message field
        self.MainMessageField = QTextEdit(self)
        self.MainMessageField.move(300,30)
        self.MainMessageField.resize(900,650)
        self.MainMessageField.setStyleSheet("font-size: 20px;")
        self.MainMessageField.setReadOnly(True)

        # Line Edit variables
        presets = ["/msg", "/msg PyroPeter", "/nick", "/nick SIMONINTHEHOUSE", "/join", "/away", "/back", "/part", "/topic", "/whois"]
        self.completer = QCompleter(presets)

        # Setting up the message field TODO Connecting the function
        self.sendMessageField = QLineEdit(self)
        self.sendMessageField.move(300,700)
        self.sendMessageField.resize(900, 70)
        self.sendMessageField.setCompleter(self.completer)
        self.sendMessageField.setStyleSheet("font-size: 20px;")

        # Setting up the joining area
        self.ChannelJOINField = QLineEdit(self)
        self.ChannelJOINField.move(50,150)
        self.ChannelJOINField.resize(200,30)

        self.ChannelJOINButton = QPushButton("Join", self)
        self.ChannelJOINButton.move(100, 200)
        self.ChannelJOINButton.clicked.connect(self.JoinChannel)

        # Setting up nickname stuff
        self.ChangeNickField = QLineEdit(self)
        self.ChangeNickField.move(50, 250)
        self.ChangeNickField.resize(200,30)

        self.ChangeNickButton = QPushButton("Change", self)
        self.ChangeNickButton.move(100, 300)
        self.ChangeNickButton.clicked.connect(self.ChangeNickName)

        
        # Setting up Labels
        self.PresetsLabel = QLabel("Presets", self)
        self.PresetsLabel.move(60,40)
        self.PresetsLabel.resize(200,40)
        self.PresetsLabel.setStyleSheet("font-size: 40px; font-weight: bold; text-decoration: underline;")

        self.ToolsLabel = QLabel("Tools", self)
        self.ToolsLabel.move(1245, 40)
        self.ToolsLabel.resize(200, 40)
        self.ToolsLabel.setStyleSheet("font-size: 40px; font-weight: bold; text-decoration: underline;")

        self.CPULabel = QLabel("CPU:", self)
        self.CPULabel.move(1250, 100)
        self.CPULabel.resize(200, 40)
        self.CPULabel.setStyleSheet("font-size: 15px; font-style: italic;")

        self.ModuleStateLabel = QLabel("", self)
        self.ModuleStateLabel.move(1250, 100)
        self.ModuleStateLabel.resize(200,40)
        self.ModuleStateLabel.setStyleSheet("font-size: 15px; font-style: italic;")

        # Setting up the send button TODO Connecting the function ... DONE
        self.sendMessageButton = QPushButton("Send Message", self)
        self.sendMessageButton.move(1250, 680)
        self.sendMessageButton.resize(120,100)
        self.sendMessageButton.setStyleSheet("font-size: 14px;")
        self.sendMessageButton.clicked.connect(self.SendMessage)

        # Setting up the module/analyse button TODO Connecting the function
        self.ModuleAnalyseButton = QPushButton("Analyse", self)
        self.ModuleAnalyseButton.move(1250, 570)
        self.ModuleAnalyseButton.resize(120,100)
        self.ModuleAnalyseButton.setStyleSheet("font-size: 14px;")
        self.ModuleAnalyseButton.clicked.connect(self.AnaylseWindow)

        # Setting up the module state button TODO Connecting the function ... DONE
        self.ModuleState = QPushButton("Module State", self)
        self.ModuleState.move(1250, 200)
        self.ModuleState.resize(120, 100)
        self.ModuleState.setStyleSheet("font-size: 14px;")
        self.ModuleState.clicked.connect(self.CheckModuleState)

        self.PrivateMSGButton = QPushButton("Private MSG", self)
        self.PrivateMSGButton.move(1250, 340)
        self.PrivateMSGButton.resize(120,100)
        self.PrivateMSGButton.setStyleSheet("font-size: 14px;")
        self.PrivateMSGButton.clicked.connect(self.PrivateMSGFunc)

        self.ClearMSGField = QPushButton("Clear", self)
        self.ClearMSGField.move(1250, 450)
        self.ClearMSGField.resize(120, 100)
        self.ClearMSGField.setStyleSheet("font-size: 14px;")
        self.ClearMSGField.clicked.connect(self.ClearMSGFieldFunc)

        # Setting up the CPU ProgressBar
        self.CPUState = QProgressBar(self)
        self.CPUState.move(1240, 130)
        self.CPUState.resize(150,30)
        self.CPUState.setStyleSheet("text-align: center; font-size: 15px;")
        self.CPUState.setValue(50)

        # Settings for the GUI
        self.setGeometry(200,200, 1400, 800)
        self.setWindowTitle("IRC-Client-Bot")
        self.setWindowIcon(QIcon("Icons\\Icon.ico"))
        self.setFixedSize(1400,800)
        self.show()

    # Setting up functions for the CPU

    def SetCPU(self, value):
        try:
            self.CPUState.setValue(int(value))
        except:
            self.CPULabel.setText("CPU: Error occurred!")

    def CPUError(self, e):
        if str(e) == "Error":
            self.CPULabel.setText("CPU: Error occurred!")
        else:
            self.CPULabel.setText("Unknown error occurred!")

    def CPUWarning(self, w):
        try:
            self.CPULabel.setText(str(w))
        except:
            self.CPULabel.setText("Unknown error occurred!")

    # Setting up module state function

    def CheckModuleState(self):
        try:
            self.ModuleStateWindow = Error_Window()
        except:
            self.ModuleStateLabel.setText("Module Window: Error!")

    def PrivateMSGFunc(self):
        #self.privMSG = PrivateMSG()
        self.Main_Socket.send_private_message(self.sendMessageField.text())

    def SendMessage(self):
        if str(self.sendMessageField.text()).startswith("/msg"):
            self.Main_Socket.send_private_message(self.sendMessageField.text())
        elif str(self.sendMessageField.text()).startswith("/nick"):
            self.Main_Socket.command_line(self.sendMessageField.text())
        elif str(self.sendMessageField.text()).startswith("/join"):
            self.Main_Socket.command_line(self.sendMessageField.text())
        elif str(self.sendMessageField.text()).startswith("/away"):
            self.Main_Socket.command_line(self.sendMessageField.text())
        elif str(self.sendMessageField.text()).startswith("/back"):
            self.Main_Socket.command_line(self.sendMessageField.text())
        elif str(self.sendMessageField.text()).startswith("/part"):
            self.Main_Socket.command_line(self.sendMessageField.text())
        elif str(self.sendMessageField.text()).startswith("/topic"):
            self.Main_Socket.command_line(self.sendMessageField.text())
        elif str(self.sendMessageField.text()).startswith("/whois"):
            self.Main_Socket.command_line(self.sendMessageField.text())
        else:
            self.Main_Socket.send_message(self.sendMessageField.text())

    def CheckConnection(self, value):
        if str(value) == "Connection established":
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Connection established" + "\n")
        else:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Connection error!"+ "\n")

    #def CheckSend(self, value):
    #    if int(value) == 1:
    #        self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Message sent successfully!" + "\n")
    #    else:
    #        self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Send error!" + "\n")

    def SetSentMessage(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Me: " + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Me: " + "Error!" + "\n")

    def SetReceivedMessage(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Receiving error!" + "\n")

        # Starting a thread for transmitting the received data
        # Implemented to avoid the GUI freezing problem
        #self.SendData = SocketThread(value)
        #self.SendData.start()


    def CheckLOG_IN(self, value):
        if str(value) == "Success":
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Logged in successfully!" + "\n")
        else:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Log-in error!" + "\n")

    def CheckNICK(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Nickname error!"+ "\n")

    def CheckJOIN(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Joining error!"+ "\n")

    def JoinedPerson(self, person):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(person) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Person join error!" + "\n")

    def QuittedPerson(self, person):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(person) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Quitting error!" + "\n")

    def SetPrivateMessage(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "PRIVATE MESSAGE Error!"+ "\n")

    def Away(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Away error!" + "\n")

    def Back(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Back error!" + "\n")

    def Part(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + "Part error!" + "\n")

    def Topic(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")

    def Whois(self, value):
        try:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")
        except:
            self.MainMessageField.setText(self.MainMessageField.toPlainText() + str(value) + "\n")

    def ClearMSGFieldFunc(self):
        self.MainMessageField.setText("")

    def JoinChannel(self):
        self.Main_Socket.join_channel(self.ChannelJOINField.text())

    def ChangeNickName(self):
        self.Main_Socket.set_nickname(self.ChangeNickField.text())

    def AnaylseWindow(self):
        self.Analyser = AnalyseWindow()

    # Setting up the keyPressEvent

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.SendMessage()
            self.sendMessageField.setText("")

    # Setting the close event

    def closeEvent(self, event):
        msg = "Exit?"
        reply = QMessageBox.question(self, msg, "Do you really want to exit the program?", QMessageBox.Yes | QMessageBox.No |
                                     QMessageBox.Cancel)
        if reply == QMessageBox.Yes:
            self.close()
        elif reply == QMessageBox.No:
            event.ignore()
        elif reply == QMessageBox.Cancel:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())