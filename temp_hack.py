
from seven_segment import CustomSevenSegment
from temp_logger import TempLogger
from relay_control import RelayControl
import time
from datetime import datetime

# {'probe': 91.4, 'ambient': 92.075, 'time': '2018-09-03 16:02:28'}

relay_pin = 21
pump = RelayControl(relay_pin)

logger = TempLogger(1)
display = CustomSevenSegment()

total_loop_time = 15
on_after_time = datetime(2018, 1, 1, 1, 3, 0).time()
on_before_time = datetime(2018, 1, 1, 1, 11, 0).time()

counter = 0
while (True):
    if (counter == 0):
        display.marquee_message('eat beef')

    try:
        # Display probe temp every second
        temp_info = logger.get_temperature_readings()

        print(temp_info)

        probe_temp = int(temp_info['probe'])
        display.display_temp(probe_temp)
    except Exception as e:
        print(e)

    current_time = datetime.now().time()
    if (current_time > on_after_time and on_before_time > current_time):
        pump.enable_relay()
    else:
        pump.disable_relay()

    counter += 1
    counter %= total_loop_time

    time.sleep(1)

