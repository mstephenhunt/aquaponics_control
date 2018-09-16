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

minutes_on = 15
minutes_off = 5
seconds_on = minutes_on * 60
seconds_off = minutes_off * 60
total_loop_time = seconds_on + seconds_off

counter = 0
while (True):
    # Display probe temp every second
    temp_info = logger.get_temperature_readings()
    probe_temp = int(temp_info['probe'])
    display.display_temp(probe_temp)

    if (counter < seconds_on):
    

    counter += 1
    counter %= total_loop_time