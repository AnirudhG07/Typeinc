import curses, string
import time
import random
import argparse
from faker import Faker 

from .text_gen import text_gen
from .result import result

def ui():
    """
    Max a good box within where the user will type
    """
    pass


def main(stdscr):
    """
    The main function will have the following steps:
    1) Handle the flags, parameters
    2) makes the UI and starts whenever the user starts typing
    3) Shows the results
    4) Ask the user if they want to continue

    """
    # Handle the flags, parameters
    parser = argparse.ArgumentParser(description='Typing speed test')
    parser.add_argument('-t', '--time', type=int, help='Time limit for the test')
    parser.add_argument('-n', '--number', type=int, help='Number of words to type')
    parser.add_argument('-a', '--alphanumeric', type= int, help='Include numbers and special characters')

    args = parser.parse_args()

    if args.n:
        text = text_gen(args.n, args.a)
    # Clear screen
    stdscr.clear()

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    words = text.split()
    selected_words = random.sample(words, 20)

    # Arrange words into lines of maximum 7 words each
    lines = [' '.join(selected_words[i:i+7]) + ' ' for i in range(0, len(selected_words), 7)]
    for i, line in enumerate(lines):
        stdscr.addstr(i, 0, line, curses.color_pair(0))

    stdscr.refresh()
    stdscr.move(0, 0)

    i = 0
    j = 0
    while i < len(lines):
        line = lines[i]
        while j < len(line):
            char = line[j]
            user_input = stdscr.getkey()
            if user_input == '\x7f':  # Backspace key
                if j > 0:
                    j -= 1
                elif i > 0:
                    i -= 1
                    j = len(lines[i]) - 1
                stdscr.addstr(i, j, line[j], curses.color_pair(0))  # Replace the character with a space
                stdscr.move(i, j)  # Move the cursor back
            else:
                if user_input == char:
                    stdscr.addstr(i, j, char, curses.color_pair(1))
                else:
                    stdscr.addstr(i, j, char, curses.color_pair(2))
                j += 1

            stdscr.refresh()

        i += 1
        j = 0

    stdscr.getch()

curses.wrapper(main)