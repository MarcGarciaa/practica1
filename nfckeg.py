import Notifications as noti
import Sensors as sen
import Database as db
from commandlist import CommandList
import time
import yaml
import json

class Nfckeg():
    def __init__(self):
        self.flow_near = None
        self.flow_out = None

        self.cl = CommandList()

        self.config()

        self.notify = []
        self.notify.append(noti.MockObject(self.cfg))
        self.notify.append(noti.TelegramChannel(self.cfg))

        self.sensors = []
        self.sensors.append(sen.Flow())
        self.sensors.append(sen.NFC())

    def dif_flow(self):
        difference = self.flow_near - self.flow_out
        return difference

    def config(self):
        with open("config.yaml") as f:
            self.cfg = yaml.load(f)
            self.token = self.cfg["telegram"]["token"]

    def next_command(self):
        try:
            return self.cl.next()
        except:
            return (None, None)


    def execute_command(self, command):
         print "Will execute", command
        words = command.split()
        first_word = words[0]
        rest_words = words[1:]
        message = None
        for a in self.sensors:
            if a.is_for_you(first_word):
                message = a.do(rest_words)
                break
        else:
            print "No t'entenc"
        return message

    def mainloop(self):
        while True:
            if N


if __name__ == "__main__"
    print "Running!"
    nfc = Nfckeg()
    nfc.mainloop()
