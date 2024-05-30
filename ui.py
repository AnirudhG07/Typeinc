import curses

def setup_window(stdscr):
    curses.initscr()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    start_y = 2  # 10 is half the height of the box
    start_x = 17  # 20 is half the width of the box
    # Create a new window for the box
    box_width=110
    box_height=30
    monitor_l2 = curses.newwin(box_height+1, box_width+2, start_y, start_x-1)
    win = curses.newwin(box_height, box_width, start_y, start_x)

    # Draw a box around the new window
    monitor_l2.box()
    monitor_l2.refresh()
    win.box()
    title = "TERMINAL TYPING SPEED TEST"
    win.addstr(start_y - 2, start_x + box_width // 3 - len(title)//2, title, curses.color_pair(5) | curses.A_BOLD)
    win.scrollok(True) # Enable scrolling

    ## Keyboard box ##
    key_box = curses.newwin(13, 99, 33, 22) # height, width, y, x
    key_box.addstr(1, 44, f"KEYBOARD", curses.color_pair(4) | curses.A_BOLD)

    key_box.box()
    key_box.refresh()

    return win, box_width, box_height

