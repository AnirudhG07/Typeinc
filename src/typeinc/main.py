import argparse
import curses
import subprocess

from .configurations.input_config import input_box
from .configurations.mainscreen import typer
from .configurations.result import result, score
from .configurations.text_gen import text_gen
from .configurations.ui import setup_window
from .scores.highscore import display_highscore, store_result

__version__ = "1.0.1"


def getsetgo(stdscr):
    numwords, alphanumeric = input_box(stdscr)

    # Test_text formatting (worse case for more than in 1 screen)
    test_text = text_gen(numwords, alphanumeric)
    total_words = len(test_text.split(" "))
    total_chars = len(test_text)
    # UI setup
    win, box_width, box_height = setup_window(stdscr)
    max_chars = (box_width-2) * (box_height-3)
    total_screens = total_chars//max_chars + 1
    tbc = '. . .' if total_screens > 1 else ''
    total_time, time_taken = 0.00, 0.00
    errors_pos = []

    for i in range(total_screens):
        test_text_formatted = test_text[i*max_chars:(i+1)*max_chars]
        # Mainscreen typing test window
        time_taken, errors_pos = typer(stdscr, test_text_formatted, total_time, tbc)
        total_time += time_taken

    wpm, grade, type_, difficulty, score=result(win, alphanumeric, total_words, total_chars, time_taken, errors_pos, test_text)
    return wpm, grade, type_, difficulty, score

def outro(stdscr):
    wpm, grade, type_, difficulty, score = getsetgo(stdscr)
    curses.endwin()

    while True: 
        to_save = input("Do you want to save the result? (y/n): ")
        if to_save.lower() == 'y' or to_save.lower() == 'yes':
            name = input("Enter your name: ")
            store_complete = store_result(name, wpm, grade, type_, difficulty, score) # difficulty is string
            if store_complete:
                print("Your score is saved. To see the top 10 scores, run `typeinc -r <difficulty level>`", flush = True)
                print("Thank you for playing!", flush = True)
            else:
                print("Some error occured while saving the score. Please try again.", flush = True)
                print("Thank you for playing!", flush = True)   
            break

        elif to_save.lower() == 'n' or to_save.lower() == 'no':
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", flush = True)
            print("What quit already? Come on give it another shot. Beat the records bruh...", flush = True)
            retry = input("Do you want to retry? (y/n): ")
            if retry.lower() == 'y' or retry.lower() == 'yes':
                subprocess.run(["typeinc"]) # Hack to restart the program, it was not working with curses.wrapper(main)
            else:
                print("Thank you for playing! Hope you had a good time.", flush = True)
            break
        else:
            print("Invalid input. Please re enter with (y/n)", flush = True)

def main():
        parser = argparse.ArgumentParser(description="""Typing Speed Test- Typeinc. A cool ncurses based typing test.
Set your own difficulty level and test the abilities of your typing skills.
For more information, visit official Github Page: https://github.come/AnirudhG07/Typeinc
Note: Please run the program on full screen mode since the UI is designed for full screen.

    ~ BE THE FASTEST TYPAA YOU COULD EVER BE ~""",
                                        formatter_class=argparse.RawTextHelpFormatter)
        # Add the flags
        parser.add_argument('-v', '--version', action='version', version=f'Typeinc - version {__version__}', help = "Show the version of the program.")

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
                    diff = float(input("Enter Difficulty Level(number): "))
                except ValueError:
                    print("Invalid input for Difficulty Level. Please enter a number.")
                    exit(0)
                try:
                    accuracy = float(input("Enter Accuracy of your typing(%): "))
                    if accuracy>100 or accuracy<0:
                        print("Invalid input for Accuracy. Please enter a number between 0 and 100.")
                        exit(0)
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
                    curses.wrapper(display_highscore, difficulty)
    
        else:
            try:
                curses.wrapper(outro)
            # error handling
            except KeyboardInterrupt:
                print("Exiting typeinc... Keyboard Interrupt")
            except Exception as e:
                if "addwstr() returned ERR" in str(e):
                    print("Please run the program on full screen mode else you will keep getting this error.")
                    print("If still this issue persists, too bad. Try running on some other computer. For most computer sizes, it should work fine.")
                # BUG: endwin() returned ERR, for linux is coming. No idea how to. Ignoring any output for it.
                if "endwin() returned ERR" in str(e):
                    pass
                else: 
                    print("An error occured: ", e)
                    
                print("Exiting typeinc...")
                    

