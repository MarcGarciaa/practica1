from Sensor import Sensor

class NFC(Sensor):
    "NFC sensor for Nfckeg"
    def __init__(self):
        super(NFC, self).__init__()

    def setup():
        """That will prepare the class to monitor the sensor. For instance,
        if the sensor must be read every n seconds, the setup method should
        prepare everything for that."""
        NFC_Ready()?s
        pass

    def get_data():
        """Returns the data read by the sensor."""
        NFCdata = "NFC_OFC1_29RFST&4LPMEMR"
        return NFCdata

    def get_cummulative():
        """If the sensor supports cumulative readings returns the amount read,
        otherwise raise error"""
        NFCcummulative = "error"
        return NFCcummulative

    def reset_cumulative():
        """Clears the cumulative readouts"""
        pass
