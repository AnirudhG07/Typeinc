import curses

def calculate_wpm_and_accuracy(correct_chars: int, correct_words:int, total_chars:int,  total_time: float, errors: int) -> tuple:
    if total_time == 0 or total_chars == 0:
        return 0, 0
    wpm = (correct_chars)/5 / (total_time / 60)
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
    50 <= diff < 100: SUPER BRUHH (X2)
    100<= diff < 500: DAMNN BRUHHH!! (XX)
    500 <= diff < 1000: U ROCK BRUHHH! (XX2)
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
        (lambda x: 50 <= x < 100, 'X2 SUPER BRUHH'),
        (lambda x: 100 <= x < 500, 'XX DAMNN BRUHHH!!'),
        (lambda x: 500 <= x < 1000, 'XX2 U ROCK BRUHHH!'),
        (lambda x: 1000 <= x, 'SXX GOD BRUH!!!')
]

    # Find the difficulty level for the given diff
    difficulty = next(d for r, d in ranges if r(diff)) # difficulty is a string

    grading = {
        'SE': [(0, 24, 'E', 'Beginner'), (24, 45, 'D', 'Novice'), (45, 65, 'C', 'Intermediate'),
               (65, 90, 'B', 'Proficient'), (90, 120, 'A', 'Advanced'), (120, 159, 'S', 'Expert'),
               (159, 20000, 'SS', 'Grandtypaa')],
        'E': [(0, 20, 'E', 'Beginner'), (20, 42, 'D', 'Novice'), (42, 54, 'C', 'Intermediate'),
              (54, 80, 'B', 'Proficient'), (80, 110, 'A', 'Advanced'), (110, 144, 'S', 'Expert'),
              (144, 20000, 'SS', 'Grandtypaa')],
        'N': [(0, 18, 'E', 'Beginner'), (17, 38, 'D', 'Novice'), (38, 48, 'C', 'Intermediate'),
              (48, 72, 'B', 'Proficient'), (72, 100, 'A', 'Advanced'), (100, 132, 'S', 'Expert'),
              (132, 20000, 'SS', 'Grandtypaa')],
        'H': [(0, 16, 'E', 'Beginner'), (15, 34, 'D', 'Novice'), (34, 42, 'C', 'Intermediate'),
              (42, 64, 'B', 'Proficient'), (64, 90, 'A', 'Advanced'), (90, 120, 'S', 'Expert'),
              (120, 20000, 'SS', 'Grandtypaa')],
        'SH': [(0, 14, 'E', 'Beginner'), (13, 30, 'D', 'Novice'), (30, 38, 'C', 'Intermediate'),
               (38, 58, 'B', 'Proficient'), (58, 80, 'A', 'Advanced'), (80, 108, 'S', 'Expert'),
               (108, 20000, 'SS', 'Grandtypaa')],
        'I': [(0, 13, 'E', 'Beginner'), (11, 26, 'D', 'Novice'), (26, 34, 'C', 'Intermediate'),
              (34, 49, 'B', 'Proficient'), (49, 72, 'A', 'Advanced'), (72, 96, 'S', 'Expert'),
              (96, 20000, 'SS', 'Grandtypaa')],
        'SI': [(0, 10, 'E', 'Beginner'), (10, 24, 'D', 'Novice'), (24, 30, 'C', 'Intermediate'),
               (30, 42, 'B', 'Proficient'), (42, 69, 'A', 'Advanced'), (69, 90, 'S', 'Expert'),
               (90, 20000, 'SS', 'Grandtypaa')],
        'X': [(0, 8, 'E', 'Beginner'), (9, 22, 'D', 'Novice'), (22, 26, 'C', 'Intermediate'),
              (26, 39, 'B', 'Proficient'), (39, 60, 'A', 'Advanced'), (60, 82, 'S', 'Expert'),
              (82, 20000, 'SS', 'Grandtypaa')],
        'X2': [(0, 6, 'E', 'Beginner'), (7, 18, 'D', 'Novice'), (18, 24, 'C', 'Intermediate'),
               (24, 36, 'B', 'Proficient'), (36, 54, 'A', 'Advanced'), (54, 75, 'S', 'Expert'),
               (75, 20000, 'SS', 'Grandtypaa')],
        'XX': [(0, 5, 'E', 'Beginner'), (6, 16, 'D', 'Novice'), (16, 20, 'C', 'Intermediate'),
               (20, 28, 'B', 'Proficient'), (28, 46, 'A', 'Advanced'), (46, 65, 'S', 'Expert'),
               (65, 20000, 'SS', 'Grandtypaa')],
        'XX2': [(0, 4, 'E', 'Beginner'), (5, 12, 'D', 'Novice'), (12, 16, 'C', 'Intermediate'),
                (16, 24, 'B', 'Proficient'), (24, 38, 'A', 'Advanced'), (38, 57, 'S', 'Expert'),
                (57, 20000, 'SS', 'Grandtypaa')],
        'SXX': [(0, 3, 'E', 'Beginner'), (3, 7, 'D', 'Novice'), (7, 10, 'C', 'Intermediate'),
                (10, 18, 'B', 'Proficient'), (18, 30, 'A', 'Advanced'), (30, 50, 'S', 'Expert'),
                (50, 20000, 'SS', 'Grandtypaa')],
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
    correct_chars = 0
    start_index = 0
    for word in words:
        if not any(i in errors_pos for i in range(start_index, start_index + len(word))):
            correct_words += 1
            correct_chars += len(word)
        start_index += len(word) + 1  # +1 to account for the space after
        try:
            if test_text[start_index-1]==' ' and start_index - 1 not in errors_pos:  # Check if the space after the word is not an error
                correct_chars += 1
        except:
            pass
    
    errors= len(errors_pos)
    wpm, accuracy = calculate_wpm_and_accuracy(correct_chars, correct_words, total_chars, total_time, errors)
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
    win.addstr(0, 18, 'Typing Test Results', curses.color_pair(4) | curses.A_BOLD)
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
    win.addstr(14, 16, 'Thank you for playing!', curses.color_pair(4) | curses.A_BOLD)
    win.refresh()

    if wpm >= 200:
        record_box = curses.newwin(4, 55, start_y + 15, start_x) # height, width, start_y, start_x
        record_box.box()
        record_box.addstr(0, 20, 'Record Breaker!', curses.color_pair(4) | curses.A_BOLD)
        record_box.addstr(1, 2, f'You have a wpm: {wpm} ', curses.color_pair(1))
        record_box.addstr(2, 2, 'Consider breaking the world record, you Grandtypaa!', curses.color_pair(5))
        record_box.refresh()
        win.refresh()
    
    if win.getch():
        return wpm, grade, type_, difficulty, score(wpm, diff, accuracy)