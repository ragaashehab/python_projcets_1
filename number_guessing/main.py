# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
game check_num, a random number is generated as the num
user has to guess the num, with hints
"""

import random
attempt_lst = []

def show_result():
    if len(attempt_lst) ==0:
        print("you are the first one")
    else:
        print("best player got it in {} attempts".format(min(attempt_lst)))

def check_num(n, g):
    if (1 > g) or (g > 20):
        result = "invalid range"
    elif (n - g) < 0:
        result = "hint: decrease your guess"
    elif (n - g) > 0:
        result = "hint: increase your guess"
    elif g == n:
        result = "you win"
    return result

def play_game():
    wanna = input('Number guessing game wanna play? YES /NO').strip()
    print(wanna.lower())
    attempt = 0
    n = random.randint(1,10)
    print (n ,attempt)
    while wanna.lower() == 'yes':
        guess = int(input("Enter your Guess a number between 1, 20: "))
        print(check_num(n,guess))
        attempt+=1
        wanna = input("try again ? YES /NO ")
    #show_result()

if __name__ == '__main__':
    play_game()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
