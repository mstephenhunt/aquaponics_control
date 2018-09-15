from relay_control import RelayControl

class Pump(RelayControl):
    def __init__(self, pin):
        RelayControl.__init__(self, pin)
        self.on_interval = 0
        self.off_interval = 0

    def set_on_off_intervals(self, on_interval, off_interval):
        self.on_interval = on_interval
        self.off_interval = off_interval