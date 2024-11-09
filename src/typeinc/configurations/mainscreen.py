import curses
import time

from .keyboard import keyboard
from .ui import setup_window


def restart(win, words, box_width, box_height):
    cursor_y, cursor_x = 1, 1
    for word in words:
        for char in word:
            if cursor_x >= box_width - 2:  # If we've reached the end of the line, move to the next line
                cursor_x = 1
                cursor_y += 1
            win.addch(cursor_y, cursor_x+1, char, curses.color_pair(3))  # Print the character in white
            cursor_x += 1
        cursor_x += 1  # Add a space after each word
        # have ' ' in position of space
        win.addch(cursor_y, cursor_x, ' ', curses.color_pair(0))
    cursor_x, cursor_y = 2, 1
    start_time = time.time()
    # Reset the cursor position
    return cursor_x, cursor_y, start_time

def typer(stdscr, test_text, total_time, tbc):
    """
    The maintyper function makes the UI and starts whenever the user starts typing and return results
    """
    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    # Clear screen
    stdscr.clear()

    # Get the size of the terminal
    win, box_width, box_height = setup_window(stdscr)

    keyboard_coordinates, getch_to_keyboard, characters = keyboard(stdscr)

    stdscr.refresh()
    win.refresh()
    words = test_text.split(" ")
    
    errors_pos = set()
    start_time = total_time
    i = 0  # The current index in the words list
    cursor_y, cursor_x = 1, 1
    win.addstr(box_height-2, box_width-6 , tbc, curses.color_pair(2) | curses.A_BOLD)
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
        if c == ord(test_text[i]) and c != ord(' '):
            win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(1)) # Color the character green
            cursor_x += 1
            if cursor_x == box_width - 1:
                cursor_x = 2
                cursor_y += 1
            i += 1
        
        elif c == ord(' '):
            if c == ord(test_text[i]):
                win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(1)) 
                cursor_x += 1
                i += 1  
                if cursor_x == box_width - 1:
                    cursor_x = 2
                    cursor_y += 1
            else:
                win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(2))
                cursor_x += 1
                if cursor_x == box_width - 1:
                    cursor_x = 2
                    cursor_y += 1
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
                i -= 1
                win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(3))  
                try:
                    if cursor_x < box_width - 2:
                        win.addch(cursor_y, cursor_x+1, test_text[i+1], curses.color_pair(3))  
                    else:
                        win.addch(cursor_y, cursor_x+1, '|', curses.color_pair(3))
                except:
                    pass
                try:
                    if cursor_x < box_width - 3:
                        win.addch(cursor_y, cursor_x+2, test_text[i+2], curses.color_pair(3))  
                    else:
                        win.addch(cursor_y, cursor_x+2, '|', curses.color_pair(3))
                except:
                    pass

        elif c == 18: # Restart the test
            if i == len(test_text)-1:
                win.addch(cursor_y, cursor_x+1, ' ')
            else:
                win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(3))
                win.addch(cursor_y, cursor_x+1, test_text[i+1], curses.color_pair(3))

            cursor_x, cursor_y, start_time = restart(win, words, box_width, box_height)
            i = 0
            errors_pos = set()
            win.refresh()
            win.move(cursor_y, cursor_x)
            win.refresh()
        
        else: # WRONG CHARACTER CHOSEN
            if test_text[i] == ' ':
                win.addch(cursor_y, cursor_x, '_', curses.color_pair(2))
                errors_pos.add(i)
                cursor_x += 1
                i += 1
                if cursor_x == box_width-1:
                    cursor_x = 2  # Reset cursor_x
                    cursor_y += 1  # Move to the next line
                    win.refresh()
            else:
                win.addch(cursor_y, cursor_x, test_text[i], curses.color_pair(2)) # Color the character red
                errors_pos.add(i)
                cursor_x += 1
                i += 1
                if cursor_x == box_width-1:
                    cursor_x = 2  # Reset cursor_x
                    cursor_y += 1  # Move to the next line
                    win.refresh()
        ### TIMER ##
        initial_time = time.time()
        stdscr.addstr(21, 138, f"{round(initial_time - start_time, 2)} seconds", curses.color_pair(5))
        stdscr.refresh()

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
                time.sleep(0.015) # For 2000 wpm, the delay would be 0.005, for delay of 0.015, the wpm would be max 800.
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
    return end_time-start_time, errors_pos
