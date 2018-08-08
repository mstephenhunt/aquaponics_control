from Adafruit_LED_Backpack import SevenSegment
import time

display = SevenSegment.SevenSegment()

display.begin()

for x in range (0, 5):
    # Clear the display buffer.
    display.clear()

    # Print a floating point number to the display.
    display.print_number_str('1111')

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    display.write_display()

    time.sleep(1)