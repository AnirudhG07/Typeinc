# Calculation of WPM

Typeinc follows Character based Formula:
<br>
It's the international standard formula for typing test, but with some tweeks. This formula is independent from exercise text. Thus it gives you a justified result with any passage your are typing.
```
WPM = (Typed Characters/5)/(Time in minutes)
## Here WPM = Word Per Minute
```
All typed entries = Total Key Strokes (or key depression).<br>
The catch is that the typed characters are basically from correct words and spaces typed.<br>

For example: The sentence you get is `"Amazing apple am intelligent"`, while your friend gets "`Hi apple this are"`. It is unfair to just see correct words, but we take the net correct characters from the correct words and then use the above formula. Thus it is independent of what sentence you get that you will get a fair WPM.

If you type 200 character(or keystroke) in 1 minutem, which are within correct words, then your typing speed will be = 200 / 5 = 40 WPM

**IMPORTANT:** In Typeinc, we just display 2 rounded decimal place, but the value used throughout has many more decimal places. Hence getting exact wpm = 40 (not displayed) is a miracle I would say.

# Time taken
The moment you start typing till the last character difference is the time taken by you. Thus it is impossible for you to backspace your last character(else you may wait for the program to automatically stop, which it won't). <br>
Time taken is calculated using the python library `time`. Thus any small difference in actual time may be caused due to code execution or time library.

When you restart, the start time is set to zero which starts again when you start typing till the end.

# Accuracy
Accuracy is calculated by -
```
Accuracy = 100 - (incorrect characters typed)/(total characters)*100
```
We do not count the character position you did pressed backspace for, although they are counted in the Correct words. So don't think their is no use of backspacing.

# Grading System Explanation

The Grading system has been set seperately for each of the difficulty levels.<br>
Look at the below given division for Grading for each difficulty level.
*Note:* 
- 20000 is set as max limit because No human or mechanical robot can achieve this. So you can try this on robots too!!!
- The limits are inclusive i.e. min_ <= wpm <= max. Hence for example if you land at exact 24 in SE level, then you will get E grade since the loop used for grading reaches E first and breaks(well intended), plus according to wpm note, getting exact 24 is a miracle.

### Super Easy Regular level (SE)

| WPM Range | Grade | Level |
| -------- | ----- | ----- |
| 0-24      | E     | Beginner |
| 24-45     | D     | Novice |
| 45-65     | C     | Intermediate |
| 65-90     | B     | Proficient |
| 90-120    | A     | Advanced |
| 120-159   | S     | Expert |
| 159-20000 | SS    | Grandtypaa |

### Easy (E)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-20      | E     | Beginner |
| 20-42     | D     | Novice |
| 42-54     | C     | Intermediate |
| 54-80     | B     | Proficient |
| 80-110    | A     | Advanced |
| 110-144   | S     | Expert |
| 144-20000 | SS    | Grandtypaa |

### Normal (N)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-18      | E     | Beginner |
| 17-38     | D     | Novice |
| 38-48     | C     | Intermediate |
| 48-72     | B     | Proficient |
| 72-100    | A     | Advanced |
| 100-132   | S     | Expert |
| 132-20000 | SS    | Grandtypaa |

### Hard (H)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-16      | E     | Beginner |
| 15-34     | D     | Novice |
| 34-42     | C     | Intermediate |
| 42-64     | B     | Proficient |
| 64-90     | A     | Advanced |
| 90-120    | S     | Expert |
| 120-20000 | SS    | Grandtypaa |

### Super Hard (SH)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-14      | E     | Beginner |
| 13-30     | D     | Novice |
| 30-38     | C     | Intermediate |
| 38-58     | B     | Proficient |
| 58-80     | A     | Advanced |
| 80-108    | S     | Expert |
| 108-20000 | SS    | Grandtypaa |

### Insane (I)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-13      | E     | Beginner |
| 11-26     | D     | Novice |
| 26-34     | C     | Intermediate |
| 34-49     | B     | Proficient |
| 49-72     | A     | Advanced |
| 72-96     | S     | Expert |
| 96-20000  | SS    | Grandtypaa |

### Super Insane (SI)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-10      | E     | Beginner |
| 10-24     | D     | Novice |
| 24-30     | C     | Intermediate |
| 30-42     | B     | Proficient |
| 42-69     | A     | Advanced |
| 69-90     | S     | Expert |
| 90-20000  | SS    | Grandtypaa |

### BRUH (X)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-8       | E     | Beginner |
| 9-22      | D     | Novice |
| 22-26     | C     | Intermediate |
| 26-39     | B     | Proficient |
| 39-60     | A     | Advanced |
| 60-82     | S     | Expert |
| 82-20000  | SS    | Grandtypaa |

### SUPER BRUHH (X2)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-6       | E     | Beginner |
| 7-18      | D     | Novice |
| 18-24     | C     | Intermediate |
| 24-36     | B     | Proficient |
| 36-54     | A     | Advanced |
| 54-75     | S     | Expert |
| 75-20000  | SS    | Grandtypaa |

### DAMNN BRUHHH!! (XX)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-5       | E     | Beginner |
| 6-16      | D     | Novice |
| 16-20     | C     | Intermediate |
| 20-28     | B     | Proficient |
| 28-46     | A     | Advanced |
| 46-65     | S     | Expert |
| 65-20000  | SS    | Grandtypaa |

### U ROCK BRUHHH! (XX2)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-4       | E     | Beginner |
| 5-12      | D     | Novice |
| 12-16     | C     | Intermediate |
| 16-24     | B     | Proficient |
| 24-38     | A     | Advanced |
| 38-57     | S     | Expert |
| 57-20000  | SS    | Grandtypaa |

### GOD BRUH!!! (SXX)

| WPM Range | Grade | Level |
| --------- | ----- | ----- |
| 0-3       | E     | Beginner |
| 3-7       | D     | Novice |
| 7-10      | C     | Intermediate |
| 10-18     | B     | Proficient |
| 18-30     | A     | Advanced |
| 30-50     | S     | Expert |
| 50-20000  | SS    | Grandtypaa |

All these numbers are well thought and come up by AnirudhG07, as mentioned before.

# Typeinc score
Typeinc score is a simple formula which gets a big decimal number which you obtain as-
```
Typeinc score = wpm * (accuracy/100) * (difficulty level multiplier factor).
```
The total time factor is already taken into consideration when calculating wpm. <br>

The multiplier factor is highly unfair to those trying lower difficulty level. Even a robot trying SE level might lose to a Novice trying SXX level in terms of `Typeinc score` Yes it is meant this way. Everything is fair in love and war. 
<br>

**_NOTE:_** Details of multiplier constant shall not be put here. 

# Text generated
For each level of difficulty, different annomalies are added to the text. The regular SE level has plain english text while rest have some ASCII characters, capitalisation mix up, etc.
<br>For the `Death texts`, referred to what you get for level > 10, all have increased difficulty and more anomalies introduced with more number of characters added. Thus even 1 word of SXX can fill up lines.<br>Also these are randomly set, it's upon your luck what length you get for your test. 

All the best bruh!
