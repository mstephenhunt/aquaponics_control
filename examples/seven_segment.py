from Adafruit_LED_Backpack import SevenSegment
import time

display = SevenSegment.SevenSegment()

display.begin()

iterator = 0
while (True):
    iterator += 1
    iterator %= 10

    iterator_as_str = str(iterator)
    display_nums = iterator_as_str + iterator_as_str + iterator_as_str + iterator_as_str

    # Clear the display buffer.
    display.clear()

    # Print a floating point number to the display.
    display.print_number_str('1111')

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    display.write_display()

    time.sleep(1)