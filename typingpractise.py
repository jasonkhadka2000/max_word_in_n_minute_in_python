import time
import random
import os
string_list=list()
def randomcharacters():
    char_length=random.randint(6,8)
    random_string=""
    for i in range(char_length):
        n=random.randint(0,25)
        random_string=random_string+chr(ord('a')+n)
    string_list.append(random_string)
    return random_string

def main():
    playagain='y'
    name = input("Enter your name: ")
    n=int(input("Enter how many minutes you want to play"))
    while playagain=='y':
        os.system("cls")
        t_end = time.time() + 60 * n
        compare_answer=list()
        score=0
        choice=int(input("Type random strings or Type a story(0 for random/1 for story)"))
        if choice==0:
            print("press enter to start")
            input()
            while time.time() < t_end:
                print(randomcharacters())
                i=input()
                compare_answer.append(i)
                os.system("cls")
            print("Your time is over")
            for i in range(len(compare_answer)):
                if compare_answer[i]==string_list[i]:
                    score=score+1
            print("your score is: {}".format(score))
        else:
            f = open('typinggame.txt', 'r')
            for line in f:
                while time.time() < t_end:
                    sentence=f.readline()
                    print(sentence)
                    string_list.append(sentence[:len(sentence)-1])
                    i=input()
                    compare_answer.append(i)
            print(string_list,compare_answer,sep="\n")
            for i in range(len(compare_answer)):
                if compare_answer[i]==string_list[i]:
                    score=score+1
            print("your typed {} correct lines".format(score))
        playagain=input("play again(y/n)")
        playagain=playagain.lower()
        string_list.clear()
        compare_answer.clear()
    print("thanks {} for playing the game".format(name))
main()











