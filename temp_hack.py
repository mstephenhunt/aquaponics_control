from seven_segment import CustomSevenSegment
from temp_logger import TempLogger
import time

# {'probe': 91.4, 'ambient': 92.075, 'time': '2018-09-03 16:02:28'}

logger = TempLogger(1)
display = CustomSevenSegment()

while (True):
    time.sleep(0.25)

    temp_info = logger.get_temperature_readings()
    probe_temp = int(temp_info['probe'])
    display.display_temp(probe_temp)