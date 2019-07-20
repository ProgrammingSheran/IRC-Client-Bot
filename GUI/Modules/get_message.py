import socket
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import *
import sys

'''class AnalyseWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.UI()

    def UI(self):

        self.Line = QTextEdit(self)
        self.Line.move(100,100)
        self.Line.resize(300,300)

        self.b1 = QPushButton("Amazon", self)
        self.b1.move(100,400)

        self.setGeometry(200,200,800,800)
        self.show()'''

# !Not necessary anymore!

class GetMessage(QThread):

    conn = pyqtSignal(str)
    message = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            self.sock.bind(("127.0.0.1", 1337))
            self.sock.listen(10)
        except:
            self.conn.emit("Connection error!")

    def get_message(self):
        try:
            while True:
                self.data, self.addr = self.sock.accept()
                self.msg = self.data.recv(1024)
                dec = self.msg.decode()
                self.message.emit(dec)
        except:
            self.conn.emit("Sock error!")

    def run(self):
        try:
            self.connect()
            self.get_message()
        except:
            self.conn.emit("Sock error!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AnalyseWindow()
    sys.exit(app.exec())