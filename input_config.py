import curses
import time
def animate_text(stdscr, y, x, text, color_pair):
    """
    Print text like animation with 0.005 sec delay.
    """
    for i in range(len(text)):
        stdscr.addstr(y, x + i, text[i], curses.color_pair(color_pair) | curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.005)
    stdscr.refresh()

def rule_box(stdscr):
    # Initialize colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    if curses.can_change_color() and curses.COLORS >= 256:
        # Initialize a color pair with a color number that corresponds to orange
        curses.init_pair(6, 208, curses.COLOR_BLACK)
        
    # Get the size of the terminal
    height, width = stdscr.getmaxyx()

    rule_text= """
    The Typinc Test is not just a typing test. You will be graded
    on the following rules which you must follow:
    1) Number of words filled in should be between 1 and 1000.
    2) Difficulty level can be any number. Absolutely any!
    Difficulty level is of the following formats:
        - level <= 0 : Super Easy (Regular) (SE)
        - 0 < level <= 2 : Easy (E)
        - 2 < level <= 4 : Normal (N)
        - 4 < level <= 6 : Hard (H)
        - 6 < level <= 9 : Super Hard (SH)
        - 9 < level <= 10 : Insane (I)
        - 10 < level < 20 : Super Insane (SI)
        - 20 <= level < 50: BRUH (X)
        - 50 <= level < 100: BRUHH (X2)
        - 100 <= level < 500: BRUHHH!! (XX)
        - 500 <= level < 1000: DAMNN BRUHHH! (XX2)
        - 1000 <= level: GOD BRUH!!! (SXX)
    3) Please see the docs for more information on grading system.
    4) Don't play with arrow keys, it might mess up the test.
                         Press q to Exit
"""
    # Make a box below input_box displaying rules
    start_y = height // 2 + 5
    start_x = width // 2 - 25
    help_box = curses.newwin(22, 70, start_y-5, start_x-1 ) # height, width, y, x
    help_box.box()
    help_box.refresh()
    stdscr.addstr(start_y-5, start_x + 30, f"RULES", curses.color_pair(5) | curses.A_BOLD)
    for i, line in enumerate(rule_text.split('\n')):
        if '-' in line: 
            stdscr.addstr( start_y-5 + i, start_x, line, curses.color_pair(2) )
        elif 'Press Enter to Exit' not in line:
            stdscr.addstr( start_y-5 + i, start_x, line, curses.color_pair(6) )
        else:
            stdscr.addstr( start_y-5 + i, start_x, line, curses.color_pair(5) | curses.A_BOLD)
    stdscr.refresh()
    return

def input_box(stdscr):
    # Initialize colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    # Get the size of the terminal
    height, width = stdscr.getmaxyx()

    Welcome_text= """
████████╗██╗   ██╗██████╗ ███████╗██╗███╗  ██╗ █████╗ 
╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝██║████╗ ██║██╔══██╗
   ██║    ╚████╔╝ ██████╔╝█████╗  ██║██╔██╗██║██║  ╚═╝
   ██║     ╚██╔╝  ██╔═══╝ ██╔══╝  ██║██║╚████║██║  ██╗
   ██║      ██║   ██║     ███████╗██║██║ ╚███║╚█████╔╝
   ╚═╝      ╚═╝   ╚═╝     ╚══════╝╚═╝╚═╝  ╚══╝ ╚════╝ 
======================================================
~Type and See how crazy your typing speed is! BRUH!!!~
======================================================
    """

    # Calculate the start coordinates for the box
    start_y = height // 2 - 5
    start_x = width // 2 - 20

    # Print the Welcome_text
    for i, line in enumerate(Welcome_text.split('\n')):
        stdscr.addstr( start_y -12 + i, start_x-2, line, curses.color_pair(4) | curses.A_BOLD)

    stdscr.refresh()
    # Draw the box
    height_inputbox=3
    stdscr.addstr(start_y - 1, start_x, "+" + "-" * 45 + "+" , curses.color_pair(1) | curses.A_BOLD)
    for i in range(start_y, start_y + height_inputbox):
        stdscr.addstr(i, start_x, "|" + " " * 45 + "|", curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(start_y + height_inputbox, start_x, "+" + "-" * 45 + "+", curses.color_pair(1) | curses.A_BOLD)

    # HELP BOX
    rule_box(stdscr)
    # Prompt for the number of words
    animate_text(stdscr, start_y, start_x + 2, "Enter the number of words: ", 5)
    curses.echo()
    num_words = ""
    while True:
        part = stdscr.getstr(start_y, start_x + 29).decode('utf-8')
        if 'q' in part:
            break
        num_words += part
        if len(part) < 36:
            break
    num_words = int(num_words)
    if num_words>=7500:
        num_words = 7500

    if num_words<=0:
        curses.endwin()
        print(f"Please explain me how you can type {num_words} words")
    elif num_words>1000:
        curses.endwin()
        print(f"Maximum number of words is 999. If you want to get yourself in trouble, then choose higher difficulty, that will increase the number of letters to type. Good Luck!")
    else:
        pass
    # Prompt for the difficulty level
    animate_text(stdscr, start_y + 1, start_x + 2, "Enter the difficulty level: ", 5)
    animate_text(stdscr, start_y + 1, start_x + 30, "0", 3)
    animate_text(stdscr, start_y + 2, start_x + 2, "Default Difficulty : 0, Enter to continue", 4)
    stdscr.move(start_y + 1, start_x + 30)
    stdscr.refresh()
    difficulty = ""
    while True:
        part = stdscr.getstr(start_y+1, start_x + 30).decode('utf-8')
        if 'q' in part:
            break
        difficulty += part
        if len(part) < 36:
            break

    # If difficulty is an empty string after stripping whitespace, set it to "0"
    if not difficulty.strip():
        difficulty = "0"

    try:
        difficulty = int(difficulty)
    except ValueError:
        curses.endwin()
        print(f"Invalid input for difficulty: {difficulty}. Please enter a valid number.")
        return
    
    stdscr.refresh()
    return num_words, difficulty
