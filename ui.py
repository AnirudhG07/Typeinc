import curses

def setup_window(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    start_y = 10  # 10 is half the height of the box
    start_x = 20  # 20 is half the width of the box
    # Create a new window for the box
    box_width=80
    box_height=20
    win = curses.newwin(box_height, box_width, start_y, start_x)

    # Draw a box around the new window
    win.box()
    title = "TERMINAL TYPING SPEED TEST"
    stdscr.addstr(start_y - 1, start_x + (box_width // 2) - (len(title) // 2), title, curses.color_pair(1))
    win.scrollok(True)

    return win, box_width, box_height