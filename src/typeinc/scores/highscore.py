import json
import datetime
import curses
import bisect
import pkg_resources
def store_result(name, wpm, grade, type_, difficulty, new_score):
    time_exact = datetime.datetime.now().isoformat()

    # Create the result dictionary
    result = {
        "time": time_exact,
        "name": name,
        "wpm": wpm,
        "grade": (grade, type_),
        "typeinc score": new_score
    }

    # Load the existing scores
    with open(pkg_resources.resource_filename(__name__, 'scores.json'), 'r') as f:
        scores = json.load(f)

    # Add the new score to the appropriate difficulty level
    difficulty = difficulty.split()[0]
    if difficulty not in scores:
        scores[difficulty] = []

    # Find the correct position to insert the new score
    scores_list = [(k, scores[difficulty][k]) for k in scores[difficulty]]

    # Find the correct position to insert the new score
    scores_list.sort(key=lambda x: x[1]['typeinc score'], reverse=True)
    position = len(scores_list) - bisect.bisect_left([score[1]['typeinc score'] for score in scores_list][::-1], new_score)

    # Insert the new score at the correct position
    scores_list.insert(position, (result['time'], result))

    # If there are more than 100 scores, remove the last one
    if len(scores_list) > 100:
        scores_list.pop()

    # Convert the list back to a dictionary
    scores[difficulty] = dict(scores_list)
    try:
        # Write the updated scores to scores.json
        with open(pkg_resources.resource_filename(__name__, 'scores.json'), 'w') as f:
            json.dump(scores, f, indent=4)
        return True
    except:    
        return False


def display_highscore(stdscr, difficulty):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    if curses.can_change_color() and curses.COLORS >= 256:
        # Initialize a color pair with a color number that corresponds to orange
        curses.init_pair(6, 208, curses.COLOR_BLACK)    
    banner = """
██╗  ██╗██╗ ██████╗ ██╗  ██╗ ██████╗ █████╗  █████╗ ██████╗ ███████╗
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
███████║██║██║  ██╗ ███████║╚█████╗ ██║  ╚═╝██║  ██║██████╔╝█████╗ 
██╔══██║██║██║  ╚██╗██╔══██║ ╚═══██╗██║  ██╗██║  ██║██╔══██╗██╔══╝  
██║  ██║██║╚██████╔╝██║  ██║██████╔╝╚█████╔╝╚█████╔╝██║  ██║███████╗
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚════╝  ╚════╝ ╚═╝  ╚═╝╚══════╝
====================================================================
                 ~ Let's see how you roll BRUH!!! ~                 
====================================================================
"""
    """"Display the highscores for the given difficulty level"""
    # Load the existing scores
    with open(pkg_resources.resource_filename(__name__, 'scores.json'), 'r') as f:
        scores = json.load(f)

    start_x = len ("Difficulty Level: ") +10

    for i, line in enumerate(banner.split('\n')):
        stdscr.addstr(i + 2, start_x, line, curses.color_pair(4) | curses.A_BOLD)
    stdscr.refresh()
    # Print the scores

    height, width = stdscr.getmaxyx()

    if difficulty not in scores or not scores[difficulty]:
        stdscr.addstr(14, start_x, "No highscores to display. Give it a shot and see your name in the list!", curses.color_pair(2) | curses.A_BOLD)
        stdscr.addstr(height -4 , start_x+5,"\n{}Press any key to exit.".format(' '*(start_x+20)), curses.color_pair(2) | curses.A_BOLD)
        stdscr.refresh()
        if stdscr.getch():
            return
        
    name_length = max(len(result['name']) for result in scores[difficulty].values())
    name_length = max(name_length, len("Name"))
    wpm_length = max(len(str(result['wpm'])) for result in scores[difficulty].values())
    grade_length = max(len(str(result['grade'])) for result in scores[difficulty].values())
    score_length = max(len(str(result['typeinc score'])) for result in scores[difficulty].values())
    score_length = max(score_length, len("Score"))
    serial_length = 4

    stdscr.addstr(12, start_x, "{}Top 10 Highscore for Typeinc Test(local)\n".format(' '*(start_x-15)), curses.color_pair(6) | curses.A_BOLD)
    stdscr.addstr(13, 20, "\n {} Difficulty Level: {}\n\n".format(' '*(start_x+20), difficulty.upper()), curses.color_pair(2) | curses.A_BOLD)
    stdscr.refresh()
    stdscr.addstr(15,start_x-3," +{}+{}+{}+{}+{}+\n".format('-'*(serial_length+2),'-'*(name_length+2), '-'*(wpm_length+2), '-'*(grade_length+2), '-'*(score_length+2)), curses.color_pair(5) | curses.A_BOLD)
    stdscr.addstr(16,start_x-3," | Sr.  | Name{} | WPM{} | Grade{} | Score{} |\n".format(' '*(name_length-4), ' '*(wpm_length-3), ' '*(grade_length-5), ' '*(score_length-5)), curses.color_pair(6) | curses.A_BOLD)
    stdscr.addstr(17,start_x-3," +{}+{}+{}+{}+{}+\n".format('-'*(serial_length+2),'-'*(name_length+2), '-'*(wpm_length+2), '-'*(grade_length+2), '-'*(score_length+2)), curses.color_pair(5) | curses.A_BOLD)
    i=18
    top10=0
    try:
        for index, time in enumerate(scores[difficulty], start=1):
            result = scores[difficulty][time]
            if top10 >= 10:
                break
            stdscr.addstr(i, start_x-3, f" | {index:<{serial_length}} | {result['name']:<{name_length}} | {result['wpm']:<{wpm_length}} | {' '.join(result['grade']):<{grade_length}} | {result['typeinc score']:<{score_length}} |\n", curses.color_pair(1) | curses.A_BOLD)
            stdscr.addstr(i+1, start_x-3," +{}+{}+{}+{}+{}+\n".format('-'*(serial_length+2), '-'*(name_length+2), '-'*(wpm_length+2), '-'*(grade_length+2), '-'*(score_length+2)), curses.color_pair(5) | curses.A_BOLD)
            i+=2
            top10+=1
    except Exception as e:
        stdscr.addstr(19,5,f"Some error occurred while displaying the highscores. Please make sure you are in full screen. Error: {e}")

    stdscr.addstr(height -4 , start_x+5,"\n{}Press any key to exit.".format(' '*(start_x+20)), curses.color_pair(2) | curses.A_BOLD)
    
    stdscr.refresh()
    if stdscr.getch():
        return