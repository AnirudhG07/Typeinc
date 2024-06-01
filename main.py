import curses
import argparse
import time, subprocess

from configurations.text_gen import text_gen
from configurations.result import *
from configurations.keyboard import *
from configurations.ui import setup_window
from configurations.input_config import *

from scores.highscore import store_result, display_highscore

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
    cursor_x, cursor_y = 2, 1
    start_time = time.time()
    # Reset the cursor position
    return cursor_x, cursor_y, start_time

def main(stdscr):
    """
    The main function will have the following steps:
    1) Handle the flags, parameters
    2) makes the UI and starts whenever the user starts typing
    3) Shows the results 
    """
    numwords, alphanumeric = input_box(stdscr)

    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    test_text = text_gen(numwords, alphanumeric)
    # words = test_text.split(" ")

    # Clear screen
    stdscr.clear()


    # Get the size of the terminal
    win, box_width, box_height = setup_window(stdscr)

    keyboard_coordinates, getch_to_keyboard, characters = keyboard(stdscr)

    stdscr.refresh()
    win.refresh()
    max_chars = (box_width -1) * (box_height-2) 
    test_text = test_text[:max_chars]  # Limit the text to the size of the box
    words = test_text.split(" ")

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
        stdscr.addstr(20, 138, f"{round(initial_time - start_time, 2)} seconds", curses.color_pair(5))
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
    wpm, grade, type_, difficulty, score=result(win, alphanumeric, total_words, total_chars, end_time-start_time, errors_pos, test_text)
    curses.endwin()
    while True:
        to_save = input("Do you want to save the result? (y/n): ")
        if to_save.lower() == 'y' or to_save.lower() == 'yes':
            name = input("Enter your name: ")
            store_result(name, wpm, grade, type_, difficulty, score) # difficulty is string
            print("Your score is saved. To see the top 10 scores, run `typeinc -r <difficulty level>`")
            print("Thank you for playing!")
            break
        elif to_save.lower() == 'n' or to_save.lower() == 'no':
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("What quit already? Come on give it another shot. Beat the records bruh...")
            retry = input("Do you want to retry? (y/n): ")
            if retry.lower() == 'y' or retry.lower() == 'yes':
                subprocess.run(["python3", "main.py"]) # Hack to restart the program, it was not working with curses.wrapper(main)
            else:
                print("Thank you for playing! Hope you had a good time.")
            break
        else:
            print("Invalid input. Please re enter with (y/n)")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Typing Speed Test- Typeinc. A cool ncurses based typing test.
Set your own difficulty level and test the abilities of your typing skills.
For more information, visit official Github Page: https://github.come/AnirudhG07/Typeinc
Note: Please run the program on full screen mode since the UI is designed for full screen.

~ BE THE FASTEST TYPAA YOU COULD EVER BE ~""",
                                    formatter_class=argparse.RawTextHelpFormatter)
    # Add the flags
    parser.add_argument('-v', '--version', action='version', version='Typeinc - version 1.0.0', help = "Show the version of the program.")

    parser.add_argument('-s', '--score', default=None, action='store_true', help='Calculate hypothetical score for input figures.')
    parser.add_argument('-w', '--words', type=int, help='Get random English words from our wordlist. Max 7500')
    parser.add_argument('-r', '--ranklist', type=str, default=None, help='Display the top 10 scores for input difficulty level.')
    
    args = parser.parse_args()

    if args.score or args.words or args.ranklist:
        if args.score:
            print("All the below entries are floating point numbers. Please fill appropriately.")
            try:
                wpm = float(input("Enter Words per Minute(WPM): "))
            except ValueError:
                print("Invalid input for Words per Minute. Please enter a number.")
                exit(0)
            try:
                diff = float(input("Enter Difficulty Level: "))
            except ValueError:
                print("Invalid input for Difficulty Level. Please enter a number.")
                exit(0)
            try:
                accuracy = float(input("Enter Accuracy of your typing(%): "))
            except ValueError:
                print("Invalid input for Accuracy. Please enter a number.")
                exit(0)
            print(f"Your calculate Typeinc score is: {score(wpm, diff, accuracy)}")
        elif args.words:
            numwords = args.words
            if numwords >=7500:
                print("The maximum number of words is 7500. We will diplsat only 7500 words.")
                numwords = 7500
            if 0<numwords<7500:
                print("Your word list is:")
                print(text_gen(int(numwords), 0))
            else:
                print("Invalid input for number of words. Please enter a number between 0 and 7500.")
                exit(0)
        elif args.ranklist:
            difficulty = args.ranklist
            difficulty = difficulty.split()[0].upper()
            if difficulty not in ['SE', 'E', 'N', 'H', 'SH', 'I', 'SI', 'X', 'X2', 'XX', 'XX2', 'SXX']:
                print("Invalid input for difficulty level. You can see the list in man page or official Github page(view link from help message)")
                exit(0)
            else:
                curses.wrapper(display_highscore,difficulty)
 
    else:
        try:
            curses.wrapper(main)
        # error handling
        except Exception as e:
            print(f"An error occurred: {e}")
            if "addwstr() returned ERR" in str(e):
                print("Please run the program on full screen mode else you will keep getting this error.")
                print("If still this issue persists, too bad. Try running on some other computer. For most computer sizes, it should work fine.")
            print("Exiting typeinc...")
        except KeyboardInterrupt:
            print("Exiting typeinc... Keyboard Interrupt")

