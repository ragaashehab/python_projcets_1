# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calculate():
    op = input("Enter the operation: Add:a , Sub:s, Div:d, Mul:m  :").strip()
    n1 = int(input("enter your first number: "))
    n2 = int(input("enter your second number: "))
    if op.lower() =="a":
        print(n1,"+", n2, "=", end = " ")
        print(n1+n2)
    elif op.lower() =="s":
        print(n1,"-", n2 , "=", end = " ")
        print(n1-n2)
    elif op.lower() == "d":
        print(n1,"/", n2, "=", end = " ")
        print(n1/n2)
    elif op.lower() == "m":
        print(n1, "*", n2 , "=", end = " ")
        print(n1*n2)
    else:
        print("entr a valid operation.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    another_operation = input("calculate operation Y/N   :").strip()
    while another_operation.lower() == "y":
        calculate()
        another_operation = input("calculate operation Y/N").strip()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
