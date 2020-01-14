# While using public transport we could see simple displays with a ticker. It often provides information about next stations and
# expected arrival time.
# Let's implement a function which will return a chunk of text to be displayed on a display of fixed width. The function should
# take text to display, width of the display and tick as a step of the ticker. The function will be called many times with tick
# parameter constantly incrementing.
# At very beginning the display is empty. At first step only one character should be displayed in the most right position and so on.
# When the message is displayed, it should be dissapear char by char to left position and return to blank state of the display.
# After that cycle should start again.
# For example: ticker('Hello world!', 10, 4)   should return '      Hell'


def create_width_of_str(width):
    space = ' '
    string = space*width
    return string

def create_full_string(text, width):
    width_string = create_width_of_str(width)
    return text + width_string

def ticker(text, width, tick):
    length_of_text = len(text)
    overall_length = length_of_text + width
    needed_tick = tick%overall_length
    string_to_display = create_width_of_str(width)
    full_string = create_full_string(text, width)
    if needed_tick == 0:
        return string_to_display
    elif needed_tick == width:
        return full_string[:width]
    elif needed_tick <= width:
        space = " "
        needed_space = space*(width-needed_tick)
        return needed_space + full_string[:needed_tick]

    else:
        return full_string[needed_tick-width:needed_tick]


def demo(text, width):
    for tick in range(100):
        print(ticker(text, width, tick))

print(demo('Beautiful is better than ugly.', 10))
