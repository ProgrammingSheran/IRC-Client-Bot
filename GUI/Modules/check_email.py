from PyQt5.QtWidgets import *
from PyQt5.Qt import Qt
from IRC.main_socket import MainIRC
import sys
from socket import gethostbyname, gaierror
import re

class CheckEmail(QWidget):

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

        self.heading = QLabel("Check Animals")
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
            self.Main_Sock.set_nickname("IRC-BOT")
            self.Main_Sock.join_channel("#testit")
        except:
            self.line.setText(self.line.toPlainText() + "Error" + "\n")

    def MainMessage(self, message):
        msg = ' '.join(message.split(":")[1:])

        known_services = ["gmail.com", "gmx.com", "outlook.com", "web.de", "mail.de", "yahoo.de", "aol.de", "spamfreemail.de",
                          "bigcitymail.de", "mailjunky.de", "firemail.de", "eclipso.de", "24-mail.de", "maili.de", "hotmail.de",
                          "emailn.de", "rediffmail.com", "kabelmail.de", "lycos.com", "skymail.de", "simbamail.de", "directbox.com",
                          "exox.de", "slucia.com", "5x2.de", "smart-mail.de", "spl.at", "t-online.de", "compu-freemail.de",
                          "x-mail.net", "k.st", "mc-free.com", "freenet.de", "k-bg.de", "overmail.de", "anpa.de", "freemailer.ch",
                          "vcmail.de", "mail4nature.org", "uims.de", "1vbb.de", "uni.de", "techmail.com", "hushmail.com",
                          "freemail-24.com", "guru.de", "email.lu", "1email.eu", "canineworld.com", "zelx.de", "sify.com",
                          "softhome.net", "kuekomail.net", "mailde.de", "mail-king.com", "oyoony.de", "oyoony.net", "oyoony.at",
                          "speed-mailer.com", "noxamail.de", "h3c.de", "arcor.de", "logomail.de", "ueberschuss.de", "chattler.de",
                          "modellraketen.de"]

        search = re.findall(r'[\w\.-]+@[\w\.-]+', msg)
        if search:
            number = 1
            for email in search:
                self.Main_Sock.send_message("Found E-Mail %s: \"%s\"" % (number, str(email)))
                domain = email.split("@")[1]
                for service in known_services:
                    if service == domain:
                        self.Main_Sock.send_message("Known E-Mail provider detected: \"%s\"" % service)
                try:
                    exists = gethostbyname(domain)
                    self.Main_Sock.send_message("Domain \"%s\" exists!" % domain)
                except gaierror:
                    self.Main_Sock.send_message("Domain \"%s\" doesn't exist!" % domain)

                number += 1

    def SockErr(self, e):
        if str(e) == "Connection established":
            self.line.setText(self.line.toPlainText() + "Connection successful!" + "\n")
        else:
            self.line.setText(self.line.toPlainText() + "Connection error!" + "\n")

    def clearField(self):
        self.line.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CheckEmail()
    sys.exit(app.exec())