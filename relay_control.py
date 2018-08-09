import RPi.GPIO as GPIO

class RelayControl:
    def __init__ (self, control_pin):
        self.control_pin = control_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(control_pin, GPIO.OUT)

    def enable_relay (self):
        GPIO.output(self.control_pin, GPIO.HIGH)

    def disable_relay (self):
        GPIO.output(self.control_pin, GPIO.LOW)
