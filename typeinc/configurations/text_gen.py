import random
import string
import pkg_resources
def death_text(n:int, a:int)->str:
    """
    Absolute RANDOM text with n words.
    """
    if a<20:
        multiplier = random.randint(1, 5)
    elif 20<=a<50:
        multiplier = random.randint(5, 10)
    elif 50<=a<100:
        multiplier = random.randint(10, 15)
    elif 100<=a<500:
        multiplier = random.randint(15, 30)
    elif 500<=a<1000:
        multiplier = random.randint(30, 100)
    else:
        multiplier = random.randint(100, 1000)
    words=[]
    chars=string.ascii_letters+string.digits+string.punctuation
    multiplier = random.randint(1, 15)
    for i in range(multiplier*n):
        word = ''.join(random.choice(chars) for _ in range(random.randint(1, 10)))
        words.append(word)
    text = " ".join(words)
    return text
        

def text_gen(n:int, alphanumeric:int)->str:
    """
    Generate random text with n words.
    Depending on the arguments given, the text can be based on -
    1) Word limit : -n <number of words>
    2) It has non alphabets like numbers, special characters, etc. : -a <difficulty level>
    """
    with open(pkg_resources.resource_filename(__name__, '../wordlist.txt'), 'r') as f:
        dictionary = f.readlines()
    # import random n words from the dictionary
    words = random.sample(dictionary, n) # type is list
    words = [word.replace('\n', '') for word in words]

    if alphanumeric < 0:
        alphanumeric = 0
    elif alphanumeric > 10:
        return death_text(n,alphanumeric)
    else:
        alphanumeric = int(alphanumeric) 

    if alphanumeric==0:
            text = " ".join(words)
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
