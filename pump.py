from relay_control import RelayControl

class Pump(RelayControl):
    def __init__(self, pin):
        RelayControl.__init__(self, pin)
        self.on_time = 0
        self.off_time = 0

    def set_on_off_intervals(self, set_on_time, set_off_time):
        self.on_time = set_on_time
        self.off_time = set_off_time