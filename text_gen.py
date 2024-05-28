import random
import string
from faker import Faker

def text_gen(n:int, alphanumeric:int)->str:
    """
    Generate random text with n words.
    Depending on the arguments given, the text can be based on -
    1) Time limit : -t <time>
    2) Word limit : -n <number of words>
    3) It has non alphabets like numbers, special characters, etc. : -a <difficulty level>
    """
    if alphanumeric < 0:
        alphanumeric = 0
    elif alphanumeric > 10:
        alphanumeric = 10
    else:
        alphanumeric = int(alphanumeric) 
    fake = Faker()
    words = fake.words(n)

    if alphanumeric==0:
            fake = Faker()
            text = " ".join(fake.words(n))
            return text
    else:
        special = string.punctuation + string.digits + string.ascii_letters
        if alphanumeric==1:
            for i in range(n):
                words[i] += random.choice(special)
        elif alphanumeric==2:
            for i in range(n):
                if random.choice([True, False]):
                    words[i] = words[i].capitalize() # Capitalize the first letter
                words[i] += random.choice(special)
        elif alphanumeric==3:
            for i in range(n):
                if random.choice([True, False]):
                    words[i] = words[i][0].capitalize() + words[i][1:-1] + words[i][-1].capitalize()
                words[i] = random.choice(special) + words[i]
        elif alphanumeric==4:
            for i in range(n):
                words[i] = ''.join(random.choice(special) if random.choice([True, False]) else c for c in words[i])
        elif alphanumeric==5:
            for i in range(n):
                words[i] = ''.join(random.choice(special) if random.choice([True, False]) else c for c in words[i].upper())
        elif alphanumeric==6:
            for i in range(n):
                words[i] = ''.join(random.choice(special) if random.choice([True, False]) else c.lower() for c in words[i])
        elif alphanumeric==7:
            for i in range(n):
                words[i] = ''.join(random.choice(special) if random.choice([True, False]) else c for c in words[i].swapcase())
        elif alphanumeric==8:
            for i in range(n):
                words[i] = ''.join(random.choice(special) if random.choice([True, False]) else c for c in words[i].title())
        elif alphanumeric==9:
            for i in range(n):
                words[i] = ''.join(random.choice(special) if random.choice([True, False]) else c for c in words[i].lower())
        elif alphanumeric==10:
            for i in range(n):
                words[i] = ''.join(random.choice(special) if random.choice([True, False]) else c.upper() for c in words[i])
                additional_chars = ''.join(random.choice(special) for _ in range(len(words[i])//2))
                for char in additional_chars:
                    position = random.randint(0, len(words[i]))
                    words[i] = words[i][:position] + char + words[i][position:]
                
        text = " ".join(words)
        return text
