import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
from datetime import datetime
from pytz import timezone

clk_pin = 17
cs_pin = 27
do_pin = 22

eastern = timezone('US/Eastern')

def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0


def get_probe_temperature (sensor):
    c_probe_temp = sensor.readTempC()
    f_probe_temp = c_to_f(c_probe_temp)

    return f_probe_temp


if __name__ == '__main__':
    sensor = MAX31855.MAX31855(clk_pin, cs_pin, do_pin)
    log_file = open("temp_log.txt", "w")

    while (True):
        # c_temp = sensor.readTempC()
        # f_temp = c_to_f(c_temp)

        f_temp = get_probe_temperature()

        formatted_timestamp = datetime.now(eastern).strftime('%Y-%m-%d %H:%M:%S')
        current_reading = "[" + formatted_timestamp + "] " + str(f_temp) + " F (" + str(c_temp) + " C)"

        print(current_reading)
        log_file.write("[" + formatted_timestamp + "] " + str(f_temp) + " F (" + str(c_temp) + " C)\n")

        time.sleep(0.25)