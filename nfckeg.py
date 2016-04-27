
class Nfckeg():
    def __init__(self):
        self.flow_near = None
        self.flow_out = None

        self.config()

    def dif_flow(self):
        difference = self.flow_near - self.flow_out
        return difference

    def config(self):
        with open("config.yaml") as f:
            self.cfg = yaml.load(f)
            self.token = self.cfg["telegram"]["token"]

    def mainloop(self):
        while True:
            if N


if __name__ == "__main__"
    print "Running!"
    nfc = Nfckeg()
    nfc.mainloop()
