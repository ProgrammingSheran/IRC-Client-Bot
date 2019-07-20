from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.Qt import QUrl
import sys
from IRC.main_socket import MainIRC
import re
import urllib.request as url
import lxml.etree as etree
from time import sleep

class MultiMsg(QThread):

    ms = pyqtSignal(str)

    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def run(self):
        for i in range(10):
            self.ms.emit(self.msg)
            sleep(1)

class CheckAmazon(QMainWindow):

    def __init__(self):
        super().__init__()

        self.Main_Sock = MainIRC("SUPERMANFORSIM", "irc.freenode.net", "#testit")
        self.Main_Sock.raw_message.connect(self.Main)
        self.Main_Sock.start()

        self.UI()

    def UI(self):

        self.line = QTextEdit(self)
        self.line.move(100,100)
        self.line.resize(200,200)

        self.AnalyseButton = QPushButton("Analyse", self)
        self.AnalyseButton.move(100,350)
        self.AnalyseButton.clicked.connect(self.threader)

        self.setGeometry(200,200,400,400)
        self.show()

    def threader(self):
        self.Main_Sock.set_nickname("SIMONS_IRC_BOT")
        self.Main_Sock.join_channel("#testit")

    def Main(self, message):

        msg = ' '.join(str(message).split(":", 1)[1:])

        if msg == "Hello":
            self.th = MultiMsg("Hello World Back")
            self.th.ms.connect(self.senderMSG)
            self.th.start()

        self.line.setText(self.line.toPlainText() + str(msg) + "\n")

    def senderMSG(self, value):
        self.Main_Sock.send_message(str(value))

    def SockErr(self, e):
        self.line.setText(self.line.toPlainText() + str(e) + "\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CheckAmazon()
    sys.exit(app.exec())


''' MATH
final = list(''.join(message))
        try:
            if str(final[0]).isdigit():
                self.Main_Sock.send_message("Computation completed: " + str(eval(message)))
            else:
                pass
        except:
            pass
            
YouTube class:
class ShowVideo(QMainWindow):

    def __init__(self, link):
        super().__init__()
        self.link = link

        self.final = str(self.link).split("=")
        print(self.final)

        self.web = QWebEngineView(self)
        self.web.move(50, 50)
        self.web.resize(300, 300)
        self.web.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.web.page().fullScreenRequested.connect(lambda request: request.accept())
        self.setCentralWidget(self.web)

        baseUrl = "local"
        htmlString = """
        <iframe width="1280" height="720" src="https://www.youtube.com/embed/%s?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>
                     """ % self.final[1]
        self.web.setHtml(htmlString, QUrl(baseUrl))
        self.web.show()

        self.setGeometry(200,200,400,400)
        self.show()
YouTube function:
        if str(message).startswith("https://www.youtube.com/watch?v="):
            self.titleParser = Title(message)
            self.titleParser.title.connect(self.getTitle)
            self.titleParser.start()

            self.openVideo = ShowVideo(message)
            self.Main_Sock.send_message("Received link: " + message)
            
YouTube title parser class (Thread):
class Title(QThread):

    title = pyqtSignal(str)

    def __init__(self, msg):
        super(Title, self).__init__()
        self.msg = msg

    def get_title(self):
        self.x = etree.HTML(url.urlopen(self.msg).read())
        self.titl = self.x.xpath("//body//span[@id='eow-title']/@title")[0]
        self.title.emit(self.titl)

    def run(self):
        self.get_title()

'''