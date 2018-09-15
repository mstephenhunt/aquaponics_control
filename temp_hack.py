from seven_segment import CustomSevenSegment
from temp_logger import TempLogger
from relay_control import RelayControl
import time
import datetime

# {'probe': 91.4, 'ambient': 92.075, 'time': '2018-09-03 16:02:28'}

relay_pin = 21
pump = RelayControl(relay_pin)

logger = TempLogger(1)
display = CustomSevenSegment()

pump.enable_relay()

while (True):
    time.sleep(0.25)

    temp_info = logger.get_temperature_readings()
    probe_temp = int(temp_info['probe'])
    display.display_temp(probe_temp)

