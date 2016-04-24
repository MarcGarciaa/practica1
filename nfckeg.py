
class Nfckeg():
    def __init__(self):
        self.flow_near = None
        self.flow_out = None

        self._get_config()

    def dif_flow(self):
        difference = self.flow_near - self.flow_out
        return difference


    def mainloop(self):
        while True:
            if N


if __name__ == "__main__"
    print "Running!"
    nfc = Nfckeg()
    nfc.mainloop()
