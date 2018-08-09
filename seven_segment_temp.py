from Adafruit_LED_Backpack import SevenSegment

class SevenSegmentTemp:
    def __init__ (self):
        self.display = SevenSegment.SevenSegment()
        self.display.begin()

    # This only accepts ints that have a length <= 3. The 
    # fourth segment on the display shows the letter F
    def display_temp (self, temp):
        if (type(temp) is int and len(str(temp)) <= 3):
            temp_string = str(temp)

            self.display.clear()
            self.display.print_number_str(temp_string)
            self.display.write_display()

        else:
            return
