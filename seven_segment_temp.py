import time
from Adafruit_LED_Backpack import SevenSegment

DIGIT_VALUES = SevenSegment.DIGIT_VALUES
DIGIT_VALUES['U'] = 0x3e # 62
DIGIT_VALUES['T'] = 0x31 # 49

class SevenSegmentTemp:
    def __init__ (self):
        self.display = SevenSegment.SevenSegment()
        self.display.begin()

    def __convert_message_to_digit_values(self, message):
        converted_message = []
        for char in message:
            converted_message.append(DIGIT_VALUES.get(str(digit).upper(), 0x00))

        return converted_message


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


    # Currently only works with 0-9, A-F, U, and T
    def marquee_message (self, message):
        # Append four spaces to end of message so 
        # that it goes fully off screen when finished
        message_with_spaces = message + '    '

        self.__convert_message_to_digit_values(message_with_spaces)

        return message_with_spaces
        # for char in message_with_spaces:
        #     current_chars.append(char)

        #     if (len(current_chars) > 4):
        #         current_chars.pop[0]

        #     self.display
