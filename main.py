import curses
import random
import argparse
import time

from text_gen import text_gen
from result import result

def ui():
    """
    Max a good box within where the user will type
    """
    pass


def main(stdscr, numwords, alphanumeric):
    """
    The main function will have the following steps:
    1) Handle the flags, parameters
    2) makes the UI and starts whenever the user starts typing
    3) Shows the results
    4) Ask the user if they want to continue

    """
    test_text = text_gen(numwords,alphanumeric)
    # Clear screen
    stdscr.clear()

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    words = test_text.split()

    errors_pos = set()
    total_chars = sum(len(word) for word in words)
    total_words = len(words)

    # Arrange words into lines of maximum 7 words each
    lines = [' '.join(words[i:i+7]) + ' ' for i in range(0, len(words), 7)]
    for i, line in enumerate(lines):
        stdscr.addstr(i, 0, line, curses.color_pair(0))

    stdscr.refresh()
    stdscr.move(0, 0)

    i = 0
    j = 0
    start_time = time.time()
    correct_words = 0
    word_start = 0

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
                stdscr.move(i, j)  # Move the cursor back
            else:
                if user_input == char:
                    stdscr.addstr(i, j, char, curses.color_pair(1))
                else:
                    stdscr.addstr(i, j, char, curses.color_pair(2)) # Red color for wrong characters
                    errors_pos.add(10*i+j)
                j += 1

            # Check if the user finished typing a word
            if char == ' ' or j == len(line):
                word_end = 10*i+j
                if not any(pos in range(word_start, word_end) for pos in errors_pos):
                    correct_words += 1
                word_start = word_end

            stdscr.refresh()

        i += 1
        j = 0
    end_time = time.time()

    # Show the results
    retry_flag=result(stdscr, correct_words, total_chars, int(end_time-start_time), len(errors_pos))
    if retry_flag== True:
        curses.endwin()
        numwords=int(input("Enter the number of words you want to type: "))
        alphanumeric=int(input("Do you want to add special characters? "))
        curses.wrapper(main, numwords, alphanumeric)
    else:
        exit(0)

if __name__ == '__main__':
    numwords=int(input("Enter the number of words you want to type: "))
    alphanumeric=int(input("Do you want to add special characters? "))
    curses.wrapper(main, numwords, alphanumeric)