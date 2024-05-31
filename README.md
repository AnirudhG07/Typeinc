# Tyepinc

Typeinc (pronounced type-in-c), an python & ncurses based tool, is your goto terminal tool to play around with your typing speed with various difficulty levels.<br>
You get an amazing UI for typing keyboard giving you a feel of both typewriters and keyboards.
<br>
Typeinc has nothing to with C, although pronounced so. It's like type-i-nc meaning type-type, I-user(you), nc-ncurses, OR maybe type-inc (Typing Incorporation), honestly I donno.
Make out whatever you want bruh!

# Previews/Screenshots
TO BE ADDED

# Features
Tyepinc provide some a next level typing test experience sitting on your terminal.
## UI
This terminal software provides a user-friendly UI with easy interactions, unless the user purposefully messes with things.<br>
It provides a really cool UI with a monitor and a KEYBOARD which gets typed when you type. (Not all keys are functional, try avoiding pressing useless buttons).

## Difficulty levels
Typeinc has the widest range of difficulty level. You can actually put any number between -infinity to +infinity (keeping in mind computer limitations). Although they are categorized so any difficulty level more than 1000 will be based on LUCK, you may get an easy level 1000 + typing test, or really nasty cause it's absolutely random.<br>
Give your best shot with the difficulty levels and have fun typing!<br>

Here is a detailed summary of the Difficulty level division.
```markdown
- Level <= 0 : Super Easy (Regular) (SE)
- 0 < Level <= 2 : Easy (E)
- 2 < Level <= 4 : Normal (N)
- 4 < Level <= 6 : Hard (H)
- 6 < Level <= 9 : Super Hard (SH)
- 9 < Level <= 10 : Insane (I)
- 10 < Level < 20 : Super Insane (SI)
- 20 <= Level < 50: BRUH (X)
- 50 <= Level < 100: SUPER BRUHH (X2)
- 100 <= Level < 500: DAMNN BRUHHH!! (XX)
- 500 <= Level < 1000: U ROCK BRUHHH! (XX2)
- 1000 <= Level: GOD BRUH!!! (SXX)
```
All the difficulties levels are set by me, including the names. This test is a total 'BRUHHH'!

**Note:** If you want to have the regular typing test, please enter without mentioning any difficulty level since Default Difficulty is set to 0.

## Grading and Typeinc score
The grading system differs for each difficulty level chosen and so is your score. The higher the difficulty level,
more the score you will obtain.<br>
Refer this tool to your friends, family and colleagues and compete with them!<br>

Please refer to `LINK TO BE ADDED` for more information regarding the grading and typeinc score.

# INSTALLATION
This is a cross-platform tool so it can be downloaded in your MacOS, Linux, Windows, etc.<br>
Follow the below guidelines to download the software
## PIP Installation
You can install this package from PyPi by running the following command0
```bash
pip install typeinc
```
If it gives any permission error, you can run using `sudo`(for Unix).
```bash
sudo pip install typeinc
```
Now you are good to go! Play by simply running typeinc by-
```bash
typeinc # to play
typeinc -h # to see help message
```

## Manual Installation
To install this tool manually, you can `git clone` this repository in your directory and run it, with the below command guidelines-
1. Clone the repository in your directory
```bash
cd /path/to/your/directory/
git clone https://github.com/AnirudhG07/Typeinc
```

2. Run `setup.py` to set the tool
```bash
python setup.py install #use python3 if required
```

Now you should be able to run the tool using `typeinc` in your terminal. Feel free to raise an issue if you face with any errors.

# Dependencies
This tool doesn't require a lot of dependencies but you need some basic requirements like
- python version >= 3.9
- curses library of python (Note: It will be automatically installed if you use the Pip Installation process)
- Some common python libraries like `random`, `argparse`, `shutil`, `string`, `time`.

If you have any doubts/facing any issue, feel free to raise an issue.

# Documentation

Check out the docs in the repository for information regarding how to use, grading system, general queries, etc. 

# Contribution

It would be great to have contributions from anyone. To make Typeinc more loved among everyone and make it better, feel free to raise an issue, discuss and make a PR.
### Contribution Guidelines
1) If you would like to raise any grading system based issues, please have a valid point using some mathematical figures to support your statements. 
    Statements like `This is unfair`, `I don't like it`, etc. will not be attended to.
2) If you feel like adding a feature or fixing bug, please put up an issue before adding a PR.

## Note regarding Grading system
All the grading, difficulty level, tyepinc score is devised by AnirudhG07(me). It has not been taken from anywhere
and all the numbers set has been made from a fair system and intuition. I honestly would give more score to a person
trying higher difficulty level cause they won't achieve a good wpm, unlike regular level where even 140-150 is possible.
<br>In no way I am also trying to equate the best possible (wpm, accuracy) of Regular Difficulty level to least possible (wpm, accuracy) of
the most Difficult level. If you wanna boast something, beat your best for `SXX`.
<br>

Thanks!