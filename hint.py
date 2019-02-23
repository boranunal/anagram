import random

def geninithint(initialWord):

    initHint = []

    for i in range(len(initialWord)):
        initHint.append('.')

    return initHint

def genRandletter(randLetList):

    random_letter = random.choice(randLetList)

    randLetList.remove(random_letter)

    return random_letter

def gen_hint_list(initialWord, random_letter, preList):

    preList[random_letter] = initialWord[random_letter]

    return preList

def print_str(hint_list):

    hint_str = ''.join(hint_list)
    print(hint_str)
