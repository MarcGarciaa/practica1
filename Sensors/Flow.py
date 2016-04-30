from Sensor import Sensor

class Flow(Sensor):
    "Flow sensor for Nfckeg"
    def __init__(self):
        super(Flow, self).__init__()
        self.flow_mesures = list()
        self.cumulative_flow = 0

    def setup():
        """That will prepare the class to monitor the sensor. For instance,
        if the sensor must be read every n seconds, the setup method should
        prepare everything for that."""
        pass

    def get_data():
        """Returns the data read by the sensor."""
        pass

    def get_cummulative():
        for flow in self.flow_mesures:
            self.cumulative_flow = self.cumulative_flow + flow
        return self.cumulative_flow

    def reset_cumulative():
        self.cumulative_flow = 0
        return self.cumulative_flow
