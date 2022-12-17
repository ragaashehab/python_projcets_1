# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
import random
def generate(pwlen):
    pwd =""
    for n in range(pwlen):
        pwd +=random.choice(string.ascii_uppercase+ string.ascii_lowercase + string.digits+ "'[@_!#$%^&*()<>?/\|}{~:]'")
    return pwd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numpwd = int(input("how many passwords you need? "))
    pwdlen = int(input("what is your password length? "))
    print([generate(pwdlen) for i in range(numpwd)])


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
