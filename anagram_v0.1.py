import random, hint
print("Choose difficulty")
diff_setting = input("Easy/Medium/Hard/IMPOSIBLE\n")

if diff_setting == "easy":

    word_file = '/home/boran/py/anagram/easy'
    WORDS = open(word_file).read().splitlines()

    chances = 3

elif diff_setting == "medium":

    word_file = '/home/boran/py/anagram/medium'
    WORDS = open(word_file).read().splitlines()

    chances = 4

elif diff_setting == "hard":
    
    word_file = '/home/boran/py/anagram/hard'
    WORDS = open(word_file).read().splitlines()

    chances = 7

else:

    word_file = '/home/boran/py/anagram/imposible'
    WORDS = open(word_file).read().splitlines()

    chances = 8

active = True

while active:
    initial = random.choice(WORDS)
    shuffledList = []
    unshuffledList = []
    randLetList = []

    #creats a list for shuffling the word
    for char in initial:
        shuffledList.append(char)
        unshuffledList.append(char)

    for n in range(len(unshuffledList)):

        randLetList.append(n)

    random.shuffle(shuffledList)
    output = ''.join(shuffledList)

    #initial hint list containing dots
    gen_hint = hint.geninithint(unshuffledList)

    #shuffled word is printed
    print(output,'\n')
    print("You have " + str(chances) + " try for this one\n\n")

    #player has 5 try to find the initial word
    for i in range(chances):
        respond = input("Your answer: ")

        #if the answer given by the player is correct
        #for loop is breaked
        if respond == initial:
            print("CORRECT!!")
            correct = 1
            break
        #if the answer given by the player is wrong
        #player is given a hint
        else:

            #test
            if chances-1-i == 0:
                break

            correct = 0
            print("TRY AGAIN")
            print("You have " + str(chances-1-i) + " more chances\n")
            print("Here is a tip")

            randomLetter = hint.genRandletter(randLetList)

            gen_hint = hint.gen_hint_list(unshuffledList,randomLetter, gen_hint)

            hint.print_str(gen_hint)


    #if the player cannot find the correct word
    #displays the answer
    if correct == 0:
        print('Correct answer was:\n' + str(initial))

    flag = input("\nType 'exit' to exit program\nPress 'Enter' to continue\n")
    if flag == 'exit':
        active = False
