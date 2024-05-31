import curses

def calculate_wpm_and_accuracy(correct_words: int, total_chars:int,  total_time: float, errors: int) -> tuple:
    if total_time == 0 or total_chars == 0:
        return 0, 0
    wpm = correct_words / (total_time / 60)
    accuracy = ((total_chars - errors) / total_chars) * 100
    return wpm, accuracy

def score(wpm, diff, accuracy):

    ranges = [
        (lambda x: x < 1, 1),
        (lambda x: 1 <= x < 3, 15),
        (lambda x: 3 <= x < 5, 50),
        (lambda x: 5 <= x < 7, 150),
        (lambda x: 7 <= x < 10, 240),
        (lambda x: 10 <= x < 20, 350),
        (lambda x: 20 <= x < 50, 480),
        (lambda x: 50 <= x < 100, 560),
        (lambda x: 100 <= x < 500, 690),
        (lambda x: 500 <= x < 1000, 850),
        (lambda x: 1000 <= x, 1000)
    ]

    # Find the multiplier for the given diff
    multiplier = next(m for r, m in ranges if r(diff))

    # Calculate the score
    score = wpm * multiplier * accuracy/100 
    return round(score,6)

def get_grade(wpm, diff):
    """
    difficulty level: 
    diff <=0 : Super Easy (Regular) (SE)
    0< diff <=2 : Easy (E)
    2< diff <=4 : Normal (N)
    4< diff <=6 : Hard (H)
    6< diff <=9 : Super Hard (SH)
    9< diff <=10 : Insane (I)
    10< diff <20 : Super Insane (SI)
    20<= diff < 50: BRUH (X)
    50 <= diff < 100: BRUHH (X2)
    100<= diff < 500: BRUHHH!! (XX)
    500 <= diff < 1000: DAMNN BRUHHH! (XX2)
    1000<= diff: GOD BRUH!!! (SXX)

    """
    # Define the ranges and difficulty levels
    ranges = [
        (lambda x: x <= 0, 'SE Super Easy(Regular)'),
        (lambda x: 0 < x < 2, 'E Easy'),
        (lambda x: 2 <= x < 4, 'N Normal'),
        (lambda x: 4 <= x < 6, 'H Hard'),
        (lambda x: 6 <= x < 9, 'SH Super Hard'),
        (lambda x: 9 <= x < 10, 'I Insane'),
        (lambda x: 10 <= x < 20, 'SI Super Insane'),
        (lambda x: 20 <= x < 50, 'X BRUH'),
        (lambda x: 50 <= x < 100, 'X2 BRUHH'),
        (lambda x: 100 <= x < 500, 'XX BRUHHH!!'),
        (lambda x: 500 <= x < 1000, 'XX2 DAMNN BRUHHH!'),
        (lambda x: 1000 <= x, 'SXX GOD BRUH!!!')
]

    # Find the difficulty level for the given diff
    difficulty = next(d for r, d in ranges if r(diff))

    grading = {
        'SE': [(0, 24, 'E', 'Beginner'), (25, 45, 'D', 'Novice'), (46, 65, 'C', 'Intermediate'),
               (61, 90, 'B', 'Proficient'), (91, 120, 'A', 'Advanced'), (121, 159, 'S', 'Expert'),
               (160, 250, 'SS', 'Grandtypaa')],
        'E': [(0, 20, 'E', 'Beginner'), (21, 39, 'D', 'Novice'), (40, 54, 'C', 'Intermediate'),
              (56, 71, 'B', 'Proficient'), (72, 90, 'A', 'Advanced'), (91, 108, 'S', 'Expert'),
              (144, 250, 'SS', 'Grandtypaa')],
        'N': [(0, 18, 'E', 'Beginner'), (17, 32, 'D', 'Novice'), (33, 48, 'C', 'Intermediate'),
              (49, 64, 'B', 'Proficient'), (65, 80, 'A', 'Advanced'), (81, 96, 'S', 'Expert'),
              (132, 250, 'SS', 'Grandtypaa')],
        'H': [(0, 16, 'E', 'Beginner'), (15, 28, 'D', 'Novice'), (29, 42, 'C', 'Intermediate'),
              (43, 56, 'B', 'Proficient'), (57, 70, 'A', 'Advanced'), (71, 84, 'S', 'Expert'),
              (120, 250, 'SS', 'Grandtypaa')],
        'SH': [(0, 14, 'E', 'Beginner'), (13, 24, 'D', 'Novice'), (25, 36, 'C', 'Intermediate'),
               (37, 48, 'B', 'Proficient'), (49, 60, 'A', 'Advanced'), (61, 72, 'S', 'Expert'),
               (108, 250, 'SS', 'Grandtypaa')],
        'I': [(0, 13, 'E', 'Beginner'), (11, 20, 'D', 'Novice'), (21, 30, 'C', 'Intermediate'),
              (31, 40, 'B', 'Proficient'), (41, 50, 'A', 'Advanced'), (51, 60, 'S', 'Expert'),
              (96, 250, 'SS', 'Grandtypaa')],
        'SI': [(0, 10, 'E', 'Beginner'), (9, 16, 'D', 'Novice'), (17, 24, 'C', 'Intermediate'),
               (25, 32, 'B', 'Proficient'), (33, 40, 'A', 'Advanced'), (41, 48, 'S', 'Expert'),
               (90, 250, 'SS', 'Grandtypaa')],
        'X': [(0, 8, 'E', 'Beginner'), (7, 12, 'D', 'Novice'), (13, 18, 'C', 'Intermediate'),
              (19, 24, 'B', 'Proficient'), (25, 30, 'A', 'Advanced'), (31, 36, 'S', 'Expert'),
              (82, 250, 'SS', 'Grandtypaa')],
        'X2': [(0, 6, 'E', 'Beginner'), (7, 16, 'D', 'Novice'), (17, 30, 'C', 'Intermediate'),
               (31, 46, 'B', 'Proficient'), (47, 65, 'A', 'Advanced'), (66, 74, 'S', 'Expert'),
               (75, 250, 'SS', 'Grandtypaa')],
        'XX': [(0, 5, 'E', 'Beginner'), (6, 18, 'D', 'Novice'), (19, 32, 'C', 'Intermediate'),
               (33, 45, 'B', 'Proficient'), (46, 55, 'A', 'Advanced'), (56, 64, 'S', 'Expert'),
               (65, 250, 'SS', 'Grandtypaa')],
        'XX2': [(0, 4, 'E', 'Beginner'), (5, 15, 'D', 'Novice'), (16, 25, 'C', 'Intermediate'),
                (26, 38, 'B', 'Proficient'), (39, 47, 'A', 'Advanced'), (48, 56, 'S', 'Expert'),
                (57, 250, 'SS', 'Grandtypaa')],
        'SXX': [(0, 3, 'E', 'Beginner'), (4, 7, 'D', 'Novice'), (8, 10, 'C', 'Intermediate'),
                (11, 18, 'B', 'Proficient'), (18, 30, 'A', 'Advanced'), (31, 49, 'S', 'Expert'),
                (50, 250, 'SS', 'Grandtypaa')],
    }
    
    grade, type_ = next((grade, type_) for min_wpm, max_wpm, grade, type_ in grading.get(difficulty.split()[0], []) if min_wpm <= wpm <= max_wpm), ('Oops', 'Retry, Some Error Occured')

    # Return the grade, type, and difficulty
    return grade, type_, difficulty
    
def result(win, diff,  total_words:int, total_chars:int, total_time:float, errors_pos:list, test_text:str)->list:
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    """"
    Show the results in the next window which includes:
    - Number of words typed
    - Number of errors
    - Time taken
    - WPM
    - Accuracy
    """
    # getting correct words
    words = test_text.split()
    correct_words = 0
    start_index = 0
    for word in words:
        if not any(i in errors_pos for i in range(start_index, start_index + len(word))):
            correct_words += 1
        start_index += len(word) + 1  # +1 to account for the space after
    
    errors= len(errors_pos)
    wpm, accuracy = calculate_wpm_and_accuracy(correct_words, total_chars, total_time, errors)
    grade_type, _ , difficulty = get_grade(wpm, diff)
    grade, type_ = grade_type[0], grade_type[1]
    # Clear the screen
    win.clear()
    win.refresh()
    # Make a box in the centre of screen and print the content in it
    height, width = win.getmaxyx()

    # Calculate the position of the box and the text
    start_y = height // 2 -5
    start_x = width // 2 

    # Create a new window for the box
    win = curses.newwin(15, 55, start_y, start_x) # height, width, start_y, start_x
    # Make a box in the centre of screen and print the content in it
    win.box()
    win.addstr(0, 15, 'Typing Test Results', curses.color_pair(4) | curses.A_BOLD)
    win.addstr(1,1,'='*52, curses.color_pair(5) | curses.A_BOLD)
    win.addstr(2, 1, f'                            ')
    win.addstr(3, 2, f'Total Words typed')
    win.addstr(3, 30, f' {total_words}', curses.color_pair(5))
    win.addstr(4, 2, f'Correct words')
    win.addstr(4, 30, f' {correct_words}', curses.color_pair(1))
    win.addstr(5, 2, f'Time taken')
    win.addstr(5, 30, f' {total_time:.2f} seconds', curses.color_pair(5))
    win.addstr(6, 2, f'Errors made(characters)')
    win.addstr(6, 30, f' {errors}', curses.color_pair(2))
    win.addstr(7, 2, f'Typing speed')
    win.addstr(7, 30, f' {round(wpm,2)} WPM', curses.color_pair(1))
    win.addstr(8, 2, f'Accuracy')
    win.addstr(8, 30, f' {accuracy}%', curses.color_pair(1))
    win.addstr(9, 2, 'Difficulty Level', curses.color_pair(3) )
    win.addstr(9, 30, f' {difficulty}', curses.color_pair(2))
    win.addstr(10, 2, f'Grade')
    win.addstr(10, 30, f' {grade} {type_}', curses.color_pair(1))
    win.addstr(11, 2, f'Typeinc Score')
    win.addstr(11, 30, f' {score(wpm, diff, accuracy)}', curses.color_pair(1))
    win.addstr(12, 15, f'Press q to exit', curses.color_pair(2))
    win.addstr(13, 1, '='*52, curses.color_pair(5) | curses.A_BOLD)
    win.addstr(14, 15, 'Thank you for playing!', curses.color_pair(4) | curses.A_BOLD)
    win.refresh()

    if wpm >= 200:
        record_box = curses.newwin(4, 55, start_y + 15, start_x) # height, width, start_y, start_x
        record_box.box()
        record_box.addstr(0, 15, 'Record Breaker!', curses.color_pair(4) | curses.A_BOLD)
        record_box.addstr(1, 15, 'You have a wpm: {wpm} ', curses.color_pair(1))
        record_box.addstr(2, 15, 'Consider breaking the world record you Grandtypaa!', curses.color_pair(5))
        record_box.refresh()
        win.refresh()