class Sensor(object):
    def __init__(self):
        super(Sensor, self).__init__()

    def do(self):
        pass

    def is_for_you(self, word):
        pass

    def setup():
        """That will prepare the class to monitor the sensor. For instance,
        if the sensor must be read every n seconds, the setup method should
        prepare everything for that."""
        pass

    def get_data():
        """Returns the data read by the sensor."""
        pass

    def get_cummulative():
        """If the sensor supports cumulative readings returns the amount read,
        otherwise raise error"""
        pass

    def reset_cumulative():
        """Clears the cumulative readouts"""
        pass
