import curses, time

def keyboard(keys):
    h, w = keys.getmaxyx()
    # Create a new window for the text box, 5 lines high and as wide as the screen

    characters = {
            "A": " / A \\ ",
            "B": " / B \\ ",
            "C": " / C \\ ",
            "D": " / D \\ ",
            "E": " / E \\ ",
            "F": " / F \\ ",
            "G": " / G \\ ",
            "H": " / H \\ ",
            "I": " / I \\ ",
            "J": " / J \\ ",
            "K": " / K \\ ",
            "L": " / L \\ ",
            "M": " / M \\ ",
            "N": " / N \\ ",
            "O": " / O \\ ",
            "P": " / P \\ ",
            "Q": " / Q \\ ",
            "R": " / R \\ ",
            "S": " / S \\ ",
            "T": " / T \\ ",
            "U": " / U \\ ",
            "V": " / V \\ ",
            "W": " / W \\ ",
            "X": " / X \\ ",
            "Y": " / Y \\ ",
            "Z": " / Z \\ ",
            "1 !": " / 1 ! \\ ",
            "2 @": " / 2 @ \\ ",
            "3 #": " / 3 # \\ ",
            "4 $": " / 4 $ \\ ",
            "5 %": " / 5 % \\ ",
            "6 ^": " / 6 ^ \\ ",
            "7 &": " / 7 & \\ ",
            "8 *": " / 8 * \\ ",
            "9 (": " / 9 ( \\ ",
            "0 )": " / 0 ) \\ ",
            "  SPC BAR  ": " / SPC BAR \\ ",
            "ENTER": " / ENTER \\ ",
            "CAPS": " / CAPS \\ ",
            " <-\\": " / <-\\ \\ ",
            "ESC": " / ESC \\ ",
            "UP": " / \u2191 \\ ",
            "DOWN": " / \u2193 \\ ",
            "LEFT": " / \u2190 \\ ",
            "RIGHT": " / \u2192 \\ ",
            "CTRL": " / CTRL \\ ",
            "ALT": " / ALT \\ ",
            "SHIFT": " / SHIFT \\ ",
            "TAB": " / TAB \\ ",
            "; :": " / ; : \\ ",
            "' \"": " / ' \" \\ ",
            ", <": " / , < \\ ",
            ". >": " / . > \\ ",
            "/ ?": " / / ? \\ ",
            "[ {": " / [ { \\ ",
            "] }": " / ] } \\ ",
            "\\ |": " / \\ | \\ ",
            "` ~": " / ` ~ \\ ",
            "- _": " / - _ \\ ",
            "= +": " / = + \\ ",
            "BACKSPACE": " / BACKSPACE \\ "
        }
    
    # Initialize the curses window
    keys = curses.initscr()

    # Define the keyboard layout in terms of coordinates
    keyboard_layout = [
        ["` ~","1 !", "2 @", "3 #", "4 $", "5 %", "6 ^", "7 &", "8 *", "9 (", "0 )"],
        ["TAB","Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[ {", "] }", "\\ |"],
        ["CAPS", "A", "S", "D", "F", "G", "H", "J", "K", "L", "; :", "' \"" ,"ENTER"],
        ["SHIFT", "Z", "X", "C", "V", "B", "N", "M", ", <", ". >", "/ ?", "- _", "= +"],
        ["CTRL", "ALT", "  SPC BAR  ", "LEFT", "DOWN", "UP", "RIGHT", "ESC", "BACKSPACE"]
    ]
    # Create a dictionary mapping each key to its coordinates
    keyboard_coordinates = {}
    h, w = keys.getmaxyx()

    for i, row in enumerate(keyboard_layout):
        y_kb = i * 2 + 35# Multiply by 2 to add a line of spacing between each row
        x_kb = 25
        for key in row:
            keyboard_coordinates[key] = (y_kb, x_kb)
            x_kb += len(key) + 5  # Add 1 for the space between keys
            
    # Iterate over the dictionary and print each key's character at its corresponding coordinates
    for key, (y_kb, x_kb) in keyboard_coordinates.items():
        if key in characters:
            keys.addstr(y_kb, x_kb, characters[key])

    # Make getch() non-blocking
    keys.nodelay(True)
    getch_to_keyboard = {
    ord('1'): "1 !", ord('!'): "1 !", ord('2'): "2 @", ord('@'): "2 @", ord('3'): "3 #", ord('#'): "3 #",
    ord('4'): "4 $", ord('$'): "4 $", ord('5'): "5 %", ord('%'): "5 %", ord('6'): "6 ^", ord('^'): "6 ^",
    ord('7'): "7 &", ord('&'): "7 &", ord('8'): "8 *", ord('*'): "8 *", ord('9'): "9 (", ord('('): "9 (",
    ord('0'): "0 )", ord(')'): "0 )", ord('-'): "- _", ord('_'): "- _", ord('='): "= +", ord('+'): "= +",
    ord('q'): "Q", ord('Q'): "Q", ord('w'): "W", ord('W'): "W", ord('e'): "E", ord('E'): "E",
    ord('r'): "R", ord('R'): "R", ord('t'): "T", ord('T'): "T", ord('y'): "Y", ord('Y'): "Y",
    ord('u'): "U", ord('U'): "U", ord('i'): "I", ord('I'): "I", ord('o'): "O", ord('O'): "O",
    ord('p'): "P", ord('P'): "P", ord('['): "[ {", ord('{'): "[ {", ord(']'): "] }", ord('}'): "] }",
    ord('a'): "A", ord('A'): "A", ord('s'): "S", ord('S'): "S", ord('d'): "D", ord('D'): "D",
    ord('f'): "F", ord('F'): "F", ord('g'): "G", ord('G'): "G", ord('h'): "H", ord('H'): "H",
    ord('j'): "J", ord('J'): "J", ord('k'): "K", ord('K'): "K", ord('l'): "L", ord('L'): "L",
    ord(';'): "; :", ord(':'): "; :", ord('\''): "' \"", ord('\"'): "' \"", ord('`'): "` ~", ord('~'): "` ~",
    ord('\\'): "\\ |", ord('|'): "\\ |", ord('z'): "Z", ord('Z'): "Z", ord('x'): "X", ord('X'): "X",
    ord('c'): "C", ord('C'): "C", ord('v'): "V", ord('V'): "V", ord('b'): "B", ord('B'): "B",
    ord('n'): "N", ord('N'): "N", ord('m'): "M", ord('M'): "M", ord(','): ", <", ord('<'): ", <",
    ord('.'): ". >", ord('>'): ". >", ord('/'): "/ ?", ord('?'): "/ ?", ord(' '): "  SPC BAR  ",
    127: "BACKSPACE", 10: "ENTER", 9: "TAB", 27: "ESC",
    ord('ă'): 'UP', ord('Ă'): 'DOWN', ord('Ą'): 'LEFT',ord('ą'): 'RIGHT'
}
    return keyboard_coordinates, getch_to_keyboard, characters

