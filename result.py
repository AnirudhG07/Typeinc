import curses

def calculate_wpm_and_accuracy(total_words: int, total_chars:int,  total_time: float, errors: int) -> tuple:
    if total_time == 0 or total_chars == 0:
        return 0, 0
    wpm = total_words / (total_time / 60)
    accuracy = round(((total_chars - errors) / total_chars) * 100,2)
    return int(wpm), accuracy

def result(stdscr, total_words:int, total_chars, total_time:float, errors:int)->list:
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    """"
    Show the results in the next window which includes:
    - Number of words typed
    - Number of errors
    - Time taken
    - WPM
    - Accuracy
    """
    wpm, accuracy = calculate_wpm_and_accuracy(total_words, total_chars, total_time, errors)
    stdscr.clear()
    stdscr.refresh()
    # Make a box in the centre of screen and print the content in it
    height, width = stdscr.getmaxyx()

    # Calculate the position of the box and the text
    start_y = height // 2 -10
    start_x = width // 2 - 25

    # Create a new window for the box
    win = curses.newwin(12, 50, start_y, start_x) 

    # Make a box in the centre of screen and print the content in it
    win.box()

    win.addstr(1, 15, 'Typing Test Results', curses.color_pair(4))
    win.addstr(2, 1, f'                            ')
    win.addstr(3, 1, f'Total Words typed: {total_words}')
    win.addstr(4, 1, f'Time taken: {total_time} seconds')
    win.addstr(6, 1, f'You made {errors} errors out of {total_chars} characters typed')
    win.addstr(7, 1, f'Typing speed: {wpm} WPM')
    win.addstr(8, 1, f'Accuracy: {accuracy}%')
    win.addstr(9, 1, f'                            ')
    win.addstr(10, 15, f'Press q to exit', curses.color_pair(3))

    win.refresh()
    stdscr.getch()
    if stdscr.getch() == ord('q'):
        # Ask if they wanna continue
        stdscr.clear()
        stdscr.refresh()
        win = curses.newwin(5, 50, start_y, start_x)
        win.attron(curses.color_pair(7))
        win.attron(curses.A_BOLD)

        # Create the border
        win.border('|', '|', '-', '-', '+', '+', '+', '+')

        # Turn off the color or attribute
        win.attroff(curses.color_pair(7))
        win.attroff(curses.A_BOLD)
        win.addstr(1, 15, 'Thank you for playing!', curses.color_pair(5))
        win.addstr(2, 1, '                          ')
        win.addstr(3, 5, 'Do you want to play again? (y/n)')
        win.refresh()
        if stdscr.getch() == ord('y'):
            return True
        else:
            return False

