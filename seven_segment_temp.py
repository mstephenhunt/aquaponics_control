import time
from Adafruit_LED_Backpack import SevenSegment

DIGIT_VALUES = SevenSegment.DIGIT_VALUES
DIGIT_VALUES['U'] = 0x3e # 62
DIGIT_VALUES['T'] = 0x78 # 120

class SevenSegmentTemp:
    def __init__ (self):
        self.display = SevenSegment.SevenSegment()
        self.display.begin()

    def __convert_message_to_digit_values(self, message):
        converted_message = []
        for char in message:
            converted_message.append(DIGIT_VALUES.get(str(char).upper(), 0x00))

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

        hex_message = self.__convert_message_to_digit_values(message_with_spaces)

        self.display.clear()

        current_chars = []
        for hex in hex_message:
            current_chars.append(hex)

            if (len(current_chars) > 4):
                current_chars.pop[0]

            self.display.set_digit_raw(0, current_chars[0])
            self.display.set_digit_raw(1, current_chars[1])
            self.display.set_digit_raw(2, current_chars[2])
            self.display.set_digit_raw(3, current_chars[3])

            self.display.write_display()
            time.sleep(0.5)

