import time
from Adafruit_LED_Backpack import SevenSegment

class SevenSegmentTemp:
    def __init__ (self):
        self.display = SevenSegment.SevenSegment()
        self.display.begin()


    # This only accepts ints that have a length <= 3. The 
    # fourth segment on the display shows the letter F
    def display_temp (self, temp):
        if (type(temp) is int and len(str(temp)) <= 3):
            temp_string = str(temp) + 'F'

            self.current_temp = temp_string

            self.display.clear()
            self.display.print_number_str(temp_string)
            self.display.write_display()

        else:
            return


    def display_message (self, message):
        self.display.clear()
        self.display.print_number_str(message)
        self.display.write_display()


    # def marquee_message (self, message):
    #     self.display.clear()
    #     current_chars = []

    #     # Append four spaces to end of message so 
    #     # that it goes fully off screen when finished
    #     message_with_spaces = message + '    '

    #     for char in message_with_spaces:
    #         current_chars.append(char)

    #         if (len(current_chars) > 4):
    #             current_chars.pop[0]

    #         self.display