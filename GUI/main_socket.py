from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtWidgets import *
import sys
import socket
import textwrap
from time import sleep
# First attempt to send private messages in a new window

class PrivateMSGThread(QThread):

    DEFAULT_SERVER = "irc.freenode.net"
    PORT = 6667
    DEAULT_CHANNEL = "#testit"

    send = pyqtSignal(int)
    conn = pyqtSignal(str)
    log_in = pyqtSignal(str)
    nick = pyqtSignal(str)

    def __init__(self, private_message, receiver):
        super().__init__()
        self.private_message = private_message
        self.receiver = receiver

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.sock.connect((self.DEFAULT_SERVER, self.PORT))
            self.conn.emit("Connection established")
            return True
        except:
            self.conn.emit("Error")
            return False

    def login(self):
        self.login_name = bytes("JOHN", "utf-8")
        try:
            self.sock.send(b"USER %s %s %s %s\n" % (self.login_name, b"Helena", b"Server", b"Pythonist"))
            self.log_in.emit("Success")
            return True
        except:
            self.log_in.emit("Error")
            return False

    def join_channel(self):
        self.irc_channel = bytes(self.DEAULT_CHANNEL, "utf-8")
        try:
            self.sock.send(b"JOIN %s\n" % self.DEAULT_CHANNEL)
            return True
        except:
            return False

    def set_nickname(self):
        self.nickname = bytes("Supermancoming", "utf-8")
        try:
            self.sock.send(b"NICK %s\n" % self.nickname)
            self.nick.emit("Success")
            return True
        except:
            self.nick.emit("Error")
            return False

    def answer_question(self):
        try:
            self.sock.send(b"PONG %s\n" % self.msg[1])
            return True
        except:
            return False

    def get_data(self):
        while True:
            self.buf = self.sock.recv(1024)
            self.dec = self.buf.decode()
            self.msg = str.split(str(self.dec))
            if self.msg[1] == b"PING":
                self.answer_question()

    def send_private_message(self, msg, receiver):
        self.private_message = bytes(msg, "utf-8")
        self.receiver  = bytes(receiver, "utf-8")
        try:
            self.sock.send(b"PRIVMSG " + b" %s" % self.receiver + b" :%s" % self.private_message + b"\n")
            self.send.emit(1)
            return True
        except:
            self.send.emit(0)

    def run(self):
        self.connect()
        self.login()
        self.join_channel()
        self.set_nickname()
        self.get_data()

class MainIRC(QThread):

    SERVER_DEFAULT = "irc.freenode.net"
    PORT = 6667
    CHANNEL_DEFAULT = "#testit"

    buffer = b""

    conn = pyqtSignal(str)
    send = pyqtSignal(int)
    sent_message = pyqtSignal(str)
    received_message = pyqtSignal(str)
    raw_message = pyqtSignal(str)
    log_in = pyqtSignal(str)
    nick = pyqtSignal(str)
    join = pyqtSignal(str)
    private_message = pyqtSignal(str)
    away_emitter = pyqtSignal(str)
    back_emitter = pyqtSignal(str)
    part_leave_emitter = pyqtSignal(str)
    topic_emitter = pyqtSignal(str)
    whois_emitter = pyqtSignal(str)
    message_entry = pyqtSignal(str)
    my_host = pyqtSignal(str)
    server_created = pyqtSignal(str)
    my_info = pyqtSignal(str)
    channel_user = pyqtSignal(str)

    joined = pyqtSignal(str)
    quitted = pyqtSignal(str)

    def __init__(self, nickname, irc_server, irc_channel):
        super().__init__()
        self.irc_server = irc_server
        self.irc_channel = irc_channel
        self.nickname = nickname

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.SERVER_DEFAULT, self.PORT))
            self.conn.emit("Connection established")
            return True
        except:
            self.conn.emit("Error")
            return False

    def send_message(self, ms):
        ms = bytes(ms, "utf-8")
        try:
            messager = ms.decode()
            if len(messager) > 400:
                divide = textwrap.wrap(messager, 400)
                for string in divide:
                    self.sock.send(b"PRIVMSG " + b" %s" % self.irc_channel + b" :%s" % bytes(string, "utf-8") + b"\n")
                    self.sent_message.emit(str(string))
                    self.send.emit(1)
            else:
                self.sock.send(b"PRIVMSG " + b" %s" % self.irc_channel + b" :%s" % ms + b"\r\n")
                self.send.emit(1)
            self.sent_message.emit(str(messager))
            return True
        except:
            self.send.emit(0)
            return False

    def send_private_message(self, message):
        split = str.split(message)
        identify = split[0]
        priv_person = split[1]
        priv_message = split[2:]
        priv_message_final = ' '.join(priv_message)

        if str(identify) == "/msg":
            try:
                self.sock.send(b"PRIVMSG" + b" %s" % bytes(priv_person, "utf-8") + b" :%s" %
                           bytes(priv_message_final, "utf-8") + b"\n")
                self.sent_message.emit("(PRIVMSG: %s) --> " % priv_person + str(priv_message_final))
            except:
                self.private_message.emit("PRIVATE-MESSAGE Error!")
        else:
            pass

    def command_line(self, message):
        split = str.split(message)
        identify = split[0]
        
        if str(identify) == "/join":
            try:
                channel = split[1]
                self.join_channel(channel)
            except:
                pass

        elif str(identify) == "/nick":
            try:
                nick = split[1]
                self.set_nickname(nick)
            except:
                pass

        elif str(identify) == "/away":
            try:
                reason = ' '.join(split[1:])
                self.away(reason)
            except:
                pass

        elif str(identify) == "/back":
            try:
                self.back()
            except:
                pass

        elif str(identify) == "/part":
            try:
                msg = split[1]
                self.part(msg)
            except:
                pass

        elif str(identify) == "/topic":
            try:
                chanelll = split[1]
                topic = ' '.join(split[2:])
                self.topic(chanelll, topic)
            except:
                pass

        elif str(identify) == "/whois":
            try:
                username = split[1]
                self.whois(username)
            except:
                pass


    def login(self):
        self.login_name = bytes("Simon", "utf-8")
        try:
            self.sock.send(b"USER %s %s %s %s\n" % (self.login_name, b"Helena", b"Server", b"Pythonist"))
            self.log_in.emit("Success")
            return True
        except:
            self.log_in.emit("Error")
            return False

    def away(self, reason):
        reason = bytes(reason, "utf-8")
        try:
            rs = reason.decode()
            self.sock.send(b"AWAY "  + b"%s" % reason + b"\r\n")
            self.away_emitter.emit("You are now marked as absent (reason): %s" % rs)
        except:
            self.away_emitter.emit("Away error")

    def back(self):
        try:
            self.sock.send(b"AWAY\r\n")
            self.back_emitter.emit("You are not marked as absent anymore!")
        except:
            self.back_emitter.emit("Back error")

    def part(self, chan):
        channeler = bytes(chan, "utf-8")
        try:
            msg = channeler.decode()
            self.sock.send(b"PART" + b" %s" % channeler + b"\r\n")
            self.part_leave_emitter.emit("You left the channel (message): %s" % msg)
        except:
            self.part_leave_emitter.emit("Part error")

    def topic(self, channel, topic):
        chanel = bytes(channel, "utf-8")
        topicc = bytes(topic, "utf-8")
        try:
            top = topicc.decode()
            self.sock.send(b"TOPIC" + b" %s" % chanel + b" %s" % topicc + b"\r\n")
            self.topic_emitter.emit("You changed the topic: %s" % top)
        except:
            self.topic_emitter.emit("Topic error")

    def whois(self, username):
        use = bytes(username, "utf-8")
        try:
            user = use.decode()
            self.sock.send(b"WHOIS" + b" %s" % use + b"\r\n")
            self.whois_emitter.emit("You requested information about: %s" % user)
        except:
            self.whois_emitter.emit("Whois error")

    def set_nickname(self, nick):
        self.nickname = bytes(nick, "utf-8")
        try:
            self.sock.send(b"NICK %s\r\n" % self.nickname)
            self.nick.emit("Set nickname" + " --> " + str(nick))
            return True
        except:
            self.nick.emit("Error")
            return False

    def join_channel(self, channel):
        self.irc_channel = bytes(channel, "utf-8")
        try:
            self.sock.send(b"JOIN %s\n" % self.irc_channel)
            self.join.emit("Joined channel" + " --> " + str(channel))
            return True
        except:
            self.join.emit("Error")
            return False

    def answer_question(self):
        try:
            self.sock.send(b"PONG %s\n" % self.msg[1])
            self.send.emit(1)
            return True
        except:
            self.send.emit("Send error")
            return False

    def get_message(self):
        try:
            data = self.sock.recv(16384)
            self.buffer += data
            if not data:
            	return

            while True:
                line, sep, buf = self.buffer.partition(b"\r\n")
                self.part_message = line.decode()
                self.msg = self.part_message.split(" ")

                if sep:
                    self.buffer = buf
                    self.grammar()
                else:
                    self.buffer = line
                    break

        except:
            self.received_message.emit("Error")

    def grammar(self):
        try:
            print(self.msg)
            self.person = ""
            if self.msg[0].startswith(":"):
                self.person = self.msg[0].split("!")[0].replace(":", "")
            else:
                pass

            self.final_message = ' '.join(self.msg[3:]).replace(":", "")

            self.raw_message.emit(self.person + ":" + str(self.final_message))
            self.new_nickname = self.msg[2].replace(":", "")
            self.new_topic = ' '.join(self.msg[3:]).replace(":", "", 1)

            if self.msg[1] == "PRIVMSG":

                if str(self.msg[2]).startswith("#"):
                    self.received_message.emit(self.person + " --> " + self.final_message)
                    #print(self.final_message)

                else:
                    self.private_message.emit(self.person + " (PRIVATE) --> " + self.final_message)

            elif self.msg[1] == "JOIN":
                self.joined.emit(self.person + " --> JOINED the channel")

            elif self.msg[1] == "QUIT":
                self.quitted.emit(self.person + " --> QUIT the channel")

            elif self.msg[1] == "NICK":
                self.nick.emit(self.person + " --> NEW NICKNAME: %s" % self.new_nickname)

            elif self.msg[1] == "PART":
                self.part_leave_emitter.emit(self.person + " --> LEFT THE CHANNEL")

            elif self.msg[1] == "TOPIC":
                self.topic_emitter.emit(self.person + " --> SET THE TOPIC TO: %s" % self.new_topic)

            elif self.msg[1] == "001":
                self.message_entry.emit("MESSAGE: %s" % ' '.join(self.msg[3:]).replace(":", ""))

            elif self.msg[1] == "002":
                self.my_host.emit("MY-HOST: %s" % ' '.join(self.msg[3:]).replace(":", ""))

            elif self.msg[1] == "003":
                self.server_created.emit("SERVER-CREATED: %s" % ' '.join(self.msg[3:]).replace(":", ""))

            elif self.msg[1] == "004":
                self.my_info.emit("MY-INFO: %s" % ' '.join(self.msg[3:]))

            elif self.msg[1] == "353":
                self.channel_user.emit("User in this channel: %s" % ', '.join(self.msg[5:]).replace(":", ""))

            elif self.msg[1] == "311":
                self.whois_emitter.emit("WHOIS [USER] --> %s (%s)" % (self.msg[3], ' '.join(self.msg[4:])))

            elif self.msg[1] == "319":
                self.whois_emitter.emit("WHOIS [CHANNEL] --> %s" % self.msg[4].replace(":", ""))

            elif self.msg[1] == "312":
                self.whois_emitter.emit("WHOIS [SERVER] --> %s %s" % (self.msg[4], ' '.join(self.msg[5:]).replace(":", "")))

            elif self.msg[1] == "671":
                self.whois_emitter.emit("WHOIS [CONNECTION-TYPE] --> %s" % ' '.join(self.msg[4:]).replace(":", ""))
                print(self.msg[1] == "671")

            elif self.msg[1] == "330":
                self.whois_emitter.emit("WHOIS [LOGGED-IN] --> %s : %s -> %s" % (self.msg[3], ' '.join(self.msg[5:]).replace(":", ""), self.msg[3]))

            elif self.msg[1] == "318":
                self.whois_emitter.emit("WHOIS --> END OF WHOIS")

            elif self.msg[1] == "332":
                self.topic_emitter.emit("Current Topic --> %s" % self.msg[4].replace(":", ""))
        except:
            pass

    def transmit_message(self):

        try:
            self.transmit_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.transmit_sock.connect(("127.0.0.1", 1337))
            self.transmit_sock.send(bytes(self.final_message, "utf-8"))
        except:
            pass

    def run(self):
        self.connect()
        self.set_nickname("SIMONINTHEHOUSE")
        self.login()
        while True:
            self.get_message()
            #self.transmit_message()

#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    w = Messaging()
#    sys.exit(app.exec())