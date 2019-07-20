import json
from PyQt5.QtWidgets import *
import sys
from PyQt5.Qt import Qt
from IRC.main_socket import MainIRC
import wikipedia
import textwrap

class CheckAnimals(QWidget):

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
            self.Main_Sock.set_nickname("SIMONS_IRC_BOT")
            self.Main_Sock.join_channel("#testit")
        except:
            self.line.setText(self.line.toPlainText() + "Error occurred!" + "\n")

    def get_summary(self, animal):

        self.animal_summary = wikipedia.summary(animal).replace("\n", "")

        return self.animal_summary

    def divide_by(self, msg_length):

        div = 2
        msg_limit = 400
        while msg_length // div > msg_limit:
            div += 1

        return div

    def MainMessage(self, message):

        msg = ' '.join(str(message).split(":")[1:])

        animals_capitalized = []
        animals_upper = []
        animals_lower = []

        try:
            animals_capitalized = json.loads(open("animals.json").read())
            animals_lower = [an.lower() for an in animals_capitalized]
            animals_upper = [ani.upper() for ani in animals_capitalized]
        except:
            self.line.setText("Error: Couldn't load the animals file!")

        try:
            splitted = str(msg).split(" ")

            for animal in animals_capitalized:
                if animal in splitted:
                    self.Main_Sock.send_message("Found animal \"%s\": https://a-z-animals.com/animals/%s " %
                                                (animal, animal))

            for animal in animals_lower:
                if animal in splitted:
                    self.Main_Sock.send_message("Found animal \"%s\": https://a-z-animals.com/animals/%s " %
                                                (animal, animal))

            for animal in animals_upper:
                if animal in splitted:
                    self.Main_Sock.send_message("Found animal \"%s\": https://a-z-animals.com/animals/%s " %
                                                (animal, animal))
        except:
            self.line.setText("An error occurred!")

        if msg.startswith("Summary") or msg.startswith("summary") or msg.startswith("SUMMARY"):
            try:
                ani = msg.split(" ")[1]
                sum = self.get_summary(ani)
                divide = textwrap.wrap(sum, 400)
                for string in divide:
                    self.Main_Sock.send_message(string)

                self.Main_Sock.send_message("Read more about %s: https://en.wikipedia.org/wiki/%s" % (ani, ani))

                self.line.setText(self.line.toPlainText() + "Summary requested for animal: %s" % ani + "\n")
                #self.result = self.divide_by(len(sum))
                #self.res = len(sum) // self.result
                #self.Main_Sock.send_message("Summary: " + str(sum))
            except:
                self.line.setText("Summary error occurred!")

        self.line.setText(self.line.toPlainText() + str(message) + "\n")

    def SockErr(self, e):
        if str(e) == "Connection established":
            self.line.setText("Connection successful!")
        else:
            self.line.setText("Connection error occurred!")

    def clearField(self):
        self.line.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CheckAnimals()
    sys.exit(app.exec())

''' That's creepy. Never ever look at this !!! First attempt to send ... argh ... large messages.
            if len(sum) > 400 and len(sum) < 450:
                    res = len(sum) // 2
                    self.Main_Sock.send_message(sum[0:res])
                    self.Main_Sock.send_message(sum[res:])
                if len(sum) > 1000 and len(sum) < 1200:
                    res = len(sum) // 3
                    self.Main_Sock.send_message(sum[0:res])
                    self.Main_Sock.send_message(sum[res:res*2])
                    self.Main_Sock.send_message(sum[res*2:])
                if len(sum) > 1200 and len(sum) < 1500:
                    res = len(sum) // 4
                    self.Main_Sock.send_message(sum[0:res])
                    self.Main_Sock.send_message(sum[res:res*2])
                    self.Main_Sock.send_message(sum[res*2: res*2*2])
                    self.Main_Sock.send_message(sum[res*2*2:])
                if len(sum) > 1500 and len(sum) < 1900:
                    res = len(sum) // 5
                    self.Main_Sock.send_message(sum[0:res])
                    self.Main_Sock.send_message(sum[res:res * 2])
                    self.Main_Sock.send_message(sum[res*2:res*2*2])
                    self.Main_Sock.send_message(sum[res*2*2: res*2**2])
                    self.Main_Sock.send_message(sum[res*2**2:])
                if len(sum) > 1900 and len(sum) < 2300:
                    res = len(sum) // 6
                    self.Main_Sock.send_message(sum[0:res])
                    self.Main_Sock.send_message(sum[res:res * 2])
                    self.Main_Sock.send_message(sum[res*2:res*2*2])
                    self.Main_Sock.send_message(sum[res*2*2: res*2**2])
                    self.Main_Sock.send_message(sum[res*2**2: res*2**3])
                    self.Main_Sock.send_message(sum[res*2**3:])
                if len(sum) > 2300 and len(sum) < 2700:
                    res = len(sum) // 7
                    self.Main_Sock.send_message(sum[0:res])
                    self.Main_Sock.send_message(sum[res:res * 2])
                    self.Main_Sock.send_message(sum[res * 2:res * 2 * 2])
                    self.Main_Sock.send_message(sum[res * 2 * 2:res * 2 ** 2])
                    self.Main_Sock.send_message(sum[res * 2 ** 2:res * 2 ** 3])
                    self.Main_Sock.send_message(sum[res * 2 ** 3:res * 2 ** 4])
                    self.Main_Sock.send_message(sum[res * 2 ** 4:])
                if len(sum) > 2700 and len(sum) < 3000:
                    res = len(sum) // 8
                    self.Main_Sock.send_message(sum[0:res])
                    self.Main_Sock.send_message(sum[res:res*2])
                    self.Main_Sock.send_message(sum[res * 2:res*2*2])
                    self.Main_Sock.send_message(sum[res * 2 * 2:res *2**2])
                    self.Main_Sock.send_message(sum[res * 2 ** 2:res*2 **3])
                    self.Main_Sock.send_message(sum[res * 2 ** 3:res*2**4])
                    self.Main_Sock.send_message(sum[res * 2 ** 4: res*2**5])
                    self.Main_Sock.send_message(sum[res*2**5:])
                if len(sum) > 3000 and len(sum) < 3500:
                    res = len(sum) // 9
                    self.Main_Sock.send_message(sum[0:res])
                    self.Main_Sock.send_message(sum[res:res*2])
                    self.Main_Sock.send_message(sum[res*2:res*2*2])
                    self.Main_Sock.send_message(sum[res*2*2:res*2**2])
                    self.Main_Sock.send_message(sum[res*2**2:res*2**3])
                    self.Main_Sock.send_message(sum[res*2**3:res*2**4])
                    self.Main_Sock.send_message(sum[res*2**4: res*2**5])
                    self.Main_Sock.send_message(sum[res*2**5: res*2**6])
                    self.Main_Sock.send_message(sum[res*2**6:])
'''