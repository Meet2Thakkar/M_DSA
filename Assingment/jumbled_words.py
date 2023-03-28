import json
import random

def choose():
    f = open("D:\PY_DSA\Assingment\wordsapi_sample.json", 'r', encoding="utf-8")
    data = json.load(f)
    words = list(data.keys())
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(p1n, p2n, p1, p2):
    print(p1n, 'Your score is ',p1)
    print(p2n, 'Your score is ',p2)

def play():
    p1name = input('P1, enter your name: ')
    p2name = input('P2, enter your name: ')
    pp1 = 0
    pp2 = 0
    turn = 0

    while (1):
        # original 1 word from the json
        picked_word = choose()
        #question
        qn = jumble(picked_word)
        print(qn)
        
        #P1
        if turn%2 == 0:
            print(p1name, " Your turn. ")
            ans = input("What's in my mind ?")
            if ans == picked_word:
                pp1+=1
                print('score is ',pp1)
            else:
                print('BLNT ans ',picked_word)
            c = int(input("Press 1 to continue or 0 to exit: "))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break 

        else:
            print(p2name, " Your turn. ")
            ans = input("What's in my mind ?")
            if ans == picked_word:
                pp2+=1
                print('score is ',pp2)
            else:
                print('BLNT ans ',picked_word)
            c = int(input("Press 1 to continue or 0 to exit: "))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break 
        turn += 1
play()