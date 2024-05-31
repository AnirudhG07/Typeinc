import curses
import random
import argparse
import time, subprocess

from text_gen import text_gen
from result import result
from keyboard import *
from ui import setup_window
from input_config import *

def main(stdscr):
    """
    The main function will have the following steps:
    1) Handle the flags, parameters :TODO 
    2) makes the UI and starts whenever the user starts typing
    3) Shows the results 
    4) Ask the user if they want to continue
    """
    numwords, alphanumeric = input_box(stdscr)

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    test_text = text_gen(numwords, alphanumeric)
    words = test_text.split(" ")

    # Clear screen
    stdscr.clear()


    # Get the size of the terminal
    win, box_width, box_height = setup_window(stdscr)

    keyboard_coordinates, getch_to_keyboard, characters = keyboard(stdscr)

    stdscr.refresh()
    win.refresh()

    # Initialize variables
    total_words = len(words)
    total_chars = len(test_text) # including spaces
    errors_pos = set()
    start_time = 0
    i = 0  # The current index in the words list
    cursor_y, cursor_x = 1, 1
    
    # Pre-print the text in the box
    for word in words:
        for char in word:
            if cursor_x >= box_width - 2:  # If we've reached the end of the line, move to the next line
                cursor_x = 1
                cursor_y += 1
            win.addch(cursor_y, cursor_x+1, char, curses.color_pair(3))  # Print the character in white
            cursor_x += 1
        cursor_x += 1  # Add a space after each word
    cursor_x, cursor_y = 2, 1
    # Reset the cursor position
    win.move(cursor_y, cursor_x)

    while i < len(test_text): 
        c = win.getch()
        if i ==0:
            start_time = time.time()
        # Check if the user is at the end of the box width
        if cursor_x >= box_width-1:
            cursor_x = 2  # Reset cursor_x
            cursor_y += 1  # Move to the next line

        if c == ord(test_text[i]) and c != ord(' '):
            win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(1)) # Color the character green
            cursor_x += 1
            i += 1
        
        elif c == ord(' '):
            if c == ord(test_text[i]):
                win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(1)) 
                cursor_x += 1
                i += 1  
            else:
                win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(2))
                cursor_x += 1
                i += 1
                errors_pos.add(i)
        elif c == 127:  # Backspace key
            #if i - 1 in errors_pos:       | ## if you want backspace to remove the error
            #    errors_pos.remove(i - 1)  |
            if cursor_x == 2:
                if cursor_y > 1:
                    cursor_y -= 1
                    cursor_x = box_width - 2
                    i -= 1
                    win.addch(cursor_y+1, 2, test_text[i+1], curses.color_pair(3))  
                    win.addch(cursor_y+1, 3, test_text[i+2], curses.color_pair(3))  
                    win.move(cursor_y, cursor_x)
                else:
                    win.addch(cursor_y, 2, test_text[i], curses.color_pair(3))  
                    win.addch(cursor_y, 3, test_text[i+1], curses.color_pair(3))  
                    win.move(cursor_y, cursor_x)
            else:
                cursor_x -= 1
                if i > 0:
                    i -= 1
                    win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(3))  
                    if cursor_x < box_width - 2:
                        win.addch(cursor_y, cursor_x+1, test_text[i+1], curses.color_pair(3))  
                    if cursor_x < box_width - 3:
                        win.addch(cursor_y, cursor_x+2, test_text[i+2], curses.color_pair(3))  
        
        else: # WRONG CHARACTER CHOSEN
            if test_text[i] == ' ':
                win.addch(cursor_y, cursor_x, '_', curses.color_pair(2))
                errors_pos.add(i)
                cursor_x += 1
                i += 1
            else:
                win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(2)) # Color the character red
                errors_pos.add(i)
                cursor_x += 1
                i += 1
   
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
        
        win.move(cursor_y, cursor_x)

    end_time = time.time()
    # Show the results
    stdscr.clear()
    stdscr.refresh()
    result(win, alphanumeric, total_words, total_chars, end_time-start_time, errors_pos, test_text)
  
if __name__ == '__main__':
    curses.wrapper(main)
