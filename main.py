import curses
import random
import argparse
import time, subprocess

from text_gen import text_gen
from result import result
from keyboard import *
from ui import setup_window


def main(stdscr, numwords, alphanumeric):
    """
    The main function will have the following steps:
    1) Handle the flags, parameters
    2) makes the UI and starts whenever the user starts typing
    3) Shows the results
    4) Ask the user if they want to continue
    """

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    test_text = text_gen(numwords,alphanumeric)
    words = test_text.split()

    # Clear screen
    stdscr.clear()

    keyboard_coordinates, getch_to_keyboard, characters = keyboard(stdscr)

    # Initialize variables
    correct_words = 0
    total_chars = len(test_text)
    errors_pos = set()
    start_time = time.time()

    # Get the size of the terminal
    height, width = stdscr.getmaxyx()
    win, box_width, box_height = setup_window(stdscr)
    # Refresh the screen to show the box
    stdscr.refresh()
    win.refresh()

    # Initialize cursor position
    cursor_y, cursor_x = 1, 2
    win.move(cursor_y, cursor_x)

    # Print the initial prompt
    win.addstr(cursor_y, cursor_x, "$ ")
    cursor_x += 2

    input_str = ""
    while True:
        # Get user input
        c = win.getch()

        if c == ord('\n'):  # If the user hits enter
            # Execute the command
            try:
                output = subprocess.check_output(input_str, shell=True)
            except subprocess.CalledProcessError as e:
                output = e.output

            # Print the output
            for line in output.decode().split('\n'):
                win.addstr(cursor_y, cursor_x, "\n"+line)
                cursor_y += 1
                if cursor_y >= box_height:  # If we've reached the bottom of the box, scroll up
                    win.scroll(1)
                    cursor_y -= 1

            # Reset cursor position to the beginning of the box
            cursor_x = 2
            cursor_y += 1
            if cursor_y >= box_height:  # If we've reached the bottom of the box, scroll up
                win.scroll(1)
                cursor_y -= 1

            # Print the prompt
            win.addstr(cursor_y, cursor_x, "zsh $ ")
            cursor_x += 2

            # Clear the input string
            input_str = ""
        elif c == ord('\b'):  # If the user hits backspace
            if cursor_x > 2:  # If we're not at the start of the line
                cursor_x -= 1
                win.delch(cursor_y, cursor_x)
                input_str = input_str[:-1]
        elif 0 <= c < 0x110000:
            # Add the character to the input string
            input_str += chr(c)
            win.addch(cursor_y, cursor_x, c)
            cursor_x += 1
            if cursor_x >= box_width:  # If we've reached the end of the line, wrap to the next line
                cursor_x = 2
                cursor_y += 1
                if cursor_y >= box_height:  # If we've reached the bottom of the box, scroll up
                    win.scroll(1)
                    cursor_y -= 1

        # Refresh the window to show the output
        win.refresh()
                    
        ########## KEYBOARD ANIMATION ##########

        # If a key was pressed
        if c != -1:
            # Convert the key to a character
            key = getch_to_keyboard.get(c)
            # If the key is in the keyboard layout
            if key in keyboard_coordinates:
                    # Get the coordinates of the key
                y, x = keyboard_coordinates[key]
                    # Erase the key at its current position
                stdscr.addstr(y, x, ' ' * len(characters[key]))
                # Print the key one line below
                stdscr.addstr(y + 1, x, characters[key])
                    # Clear the screen and refresh
                stdscr.refresh()
                time.sleep(0.02)
                # Erase the key at the new position
                stdscr.addstr(y + 1, x, ' ' * len(characters[key]))
                # Print the key at its original position
                stdscr.addstr(y, x, characters[key])
                # Clear the screen and refresh
                stdscr.refresh()

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
