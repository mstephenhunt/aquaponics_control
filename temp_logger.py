import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
from datetime import datetime
from pytz import timezone

class TempLogger:
    def __init__ (self, logging_period):
        __clk_pin = 17
        __cs_pin = 27
        __do_pin = 22

        # logging period is provided in seconds
        self.logging_period = logging_period

        self.sensor = MAX31855.MAX31855(__clk_pin, __cs_pin, __do_pin)


    def __c_to_f (self, c):
        return c * 9.0 / 5.0 + 32.0


    def __get_probe_temperature (self):
        c_probe_temp = self.sensor.readTempC()
        f_probe_temp = self.__c_to_f(c_probe_temp)

        return f_probe_temp


    def __get_ambient_temperature (self):
        c_ambient_temp = self.sensor.readInternalC()
        f_ambient_temp = self.__c_to_f(c_ambient_temp)

        return f_ambient_temp


    def get_temperature_readings (self):
        probe_temp = self.__get_probe_temperature()
        ambient_temp = self.__get_ambient_temperature()


        eastern = timezone('US/Eastern')
        formatted_timestamp = datetime.now(eastern).strftime('%Y-%m-%d %H:%M:%S')
        current_reading = "{ \"time\": " + formatted_timestamp + ",\"probe\": " + str(probe_temp) + ",\"ambient\": " + str(ambient_temp) + "}\n"

        return current_reading


    def log_temperature (self):
        log_file = open("temp_log.txt", "a+")

        while(True):
            current_reading = self.get_temperature_readings()
            log_file.write(current_reading)
            time.sleep(self.logging_period)
