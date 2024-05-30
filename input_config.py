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
 Please run this in full screen mode else it'll crash
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
    stdscr.addstr(start_y - 1, start_x, "+" + "-" * 45 + "+" , curses.color_pair(1) | curses.A_BOLD)
    for i in range(start_y, start_y + 4):
        stdscr.addstr(i, start_x, "|" + " " * 45 + "|", curses.color_pair(2) | curses.A_BOLD)
    stdscr.addstr(start_y + 4, start_x, "+" + "-" * 45 + "+", curses.color_pair(1) | curses.A_BOLD)

    # Prompt for the number of words
    animate_text(stdscr, start_y, start_x + 2, "Enter the number of words: ", 5)
    curses.echo()
    num_words = ""
    while True:
        part = stdscr.getstr(start_y, start_x + 29).decode('utf-8')
        num_words += part
        if len(part) < 36:
            break
    num_words = int(num_words)

    if num_words<=0:
        curses.endwin()
        print(f"Please explain me how you can type {num_words} words")
    elif num_words>1000:
        curses.endwin()
        print(f"Maximum number of words is 1000. If you want to get yourself in trouble, then choose higher difficulty, that will increase the number of letters to type. Good Luck!")
    else:
        pass
    # Prompt for the difficulty level
    animate_text(stdscr, start_y + 1, start_x + 2, "Enter the difficulty level: ", 5)
    animate_text(stdscr, start_y + 1, start_x + 30, "0", 3)
    difficulty = ""
    while True:
        part = stdscr.getstr(start_y+1, start_x + 30).decode('utf-8')
        difficulty += part
        if len(part) < 36:
            break
    difficulty = int(difficulty)

    stdscr.refresh()
    return num_words, difficulty
