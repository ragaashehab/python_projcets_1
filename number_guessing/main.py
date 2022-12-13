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
        m = min(attempt_lst)
        print("best player got it in {} attempts".format(m))

def play_game():
    n = random.randint(1, 10)
    print(n)
    attempt = 0
    guess_again = "y"
    while attempt <= 10:
        g = int(input("Enter your Guess a number between 1, 10: "))
        if (1 > g) or (g > 10):
            print("invalid range")
            attempt +=1
        elif (n - g) < 0:
            print("hint: decrease your guess")
            attempt += 1
        elif (n - g) > 0:
            print("hint: increase your guess")
            attempt += 1
        elif g == n:
            print("you won")
            return attempt
    return attempt

if __name__ == '__main__':
    wanna = input('Number guessing game wanna play? Y/N ').strip()
    while wanna.lower() == "y":
        attempt = play_game()
        print("you got it in {} attempts ".format(attempt))
        attempt_lst.append(attempt)
        show_result()
        wanna = input('Number guessing game wanna play? Y/N ').strip()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
