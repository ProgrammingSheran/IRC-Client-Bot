from PyQt5.QtWidgets import *
from IRC.main_socket import MainIRC
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.Qt import QUrl
from PyQt5.Qt import Qt
import lxml.etree as etree
import urllib.request as url
import sys

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

class CheckYouTube(QWidget):

    def __init__(self):
        super().__init__()

        try:
            self.Main_Sock = MainIRC("SUPERMANFORSIM", "irc.freenode.net", "#testit")
            self.Main_Sock.raw_message.connect(self.MainMessage)
            self.Main_Sock.conn.connect(self.SockErr)
            self.Main_Sock.start()
        except:
            self.line.setText(self.line.toPlainText() + "Socket error!" + "\n")

        self.UI()

    def UI(self):

        layout = QVBoxLayout()

        self.heading = QLabel("Check YouTube")
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setStyleSheet("font-size: 40px; font-weight: bold;")

        self.line = QTextEdit()
        self.line.move(100,100)
        self.line.resize(200,200)
        self.line.setStyleSheet("font-size: 20px;")
        self.line.setReadOnly(True)

        self.AnalyseButton = QPushButton("Start Analysing")
        self.AnalyseButton.move(100, 350)
        self.AnalyseButton.clicked.connect(self.threader)
        self.AnalyseButton.setStyleSheet("padding: 15 15px; font-size: 20px;")

        self.deleteButton = QPushButton("Clear")
        self.deleteButton.setStyleSheet("padding: 15 15px; font-size: 20px;")
        self.deleteButton.clicked.connect(self.clearField)

        self.liner = QLineEdit()
        self.liner.setStyleSheet("padding: 10 10px; font-size: 20px;")
        self.liner.setPlaceholderText("IRC-Channel")

        layout.addWidget(self.heading)
        layout.addWidget(self.line)
        layout.addWidget(self.AnalyseButton)
        layout.addWidget(self.deleteButton)
        layout.addWidget(self.liner)

        self.setLayout(layout)

        self.setGeometry(200,200,600,600)
        self.show()

    def threader(self):
        try:
            self.Main_Sock.set_nickname("SIMONS_IRC_BOT")
            self.Main_Sock.join_channel("#testit")
        except:
            self.line.setText(self.line.toPlainText() + "Error occurred!" + "\n")

    def MainMessage(self, message):

        msg = ' '.join(str(message).split(":", 1)[1:])

        if str(msg).startswith("https://www.youtube.com/watch?v="):
            self.titleParser = Title(msg)
            self.titleParser.title.connect(self.getTitle)
            self.titleParser.start()

            self.openVideo = ShowVideo(msg)
            self.Main_Sock.send_message("Received link: " + msg)

    def getTitle(self, title):
        self.Main_Sock.send_message("Found title for the video: %s" % str(title))

    def SockErr(self, e):
        if str(e) == "Connection established":
            self.line.setText("Connection successful!")
        else:
            self.line.setText("Connection error occurred!")

    def clearField(self):
        self.line.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CheckYouTube()
    sys.exit(app.exec())