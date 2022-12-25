# importing the tkinter module
import math
from tkinter import *

# initializing th TKinter
root= Tk()
root.title("MY CALCULATOR")
# setting the width and height of
root.geometry("430x500")
# declaring an empty string var
expression =""

# defining function which will set expressions
def setexpression(num):
    global expression
    expression = expression +str(num)
    value.set(expression)

#The eval() method parses the expression passed to
# this method and runs python expression (code) within the program.
#StringVar() is one of those tkinter types.
#strVar = StringVar() Holds a string an empty string ""
#intVar = IntVar() dbVar = DoubleVar() blVar = BooleanVar()

# defining a function to calculate the express
def calculator():
    try:
        global expression
        answer = str(eval(expression))
        value.set(answer)
    except:
        value.set("enter correct expression ")
        expression= ""

def squart():
    try:
        global expression
        answer = str(math.sqrt(eval(expression)))
        value.set(answer)
    except:
        value.set("enter correct expression ")
        expression= ""

# function to clear everything
def clear():
    global expression
    expression = ""
    value.set(expression)


# declaring font variables as ("Language", size)
large_font = ('Verdana', 15)
small_font = ('Verdana', 10)

# declaring variable to take value of express
value = StringVar(value = "enter expression")

# entry widget to take expression from user and to show
# calculation
Entry(root, textvariable= value , font= large_font).grid(row=0,
    column=0, columnspan=4, ipadx=70)
Button(root, text="+", fg= "red", command = lambda :
    setexpression("+"), height=4, width= 8).grid(row= 1, column= 0, pady= 10)
Button(root, text="-", fg="red", command=lambda:
    setexpression("-"), height=4, width=8).grid(row=2, column=0, pady=10)
Button(root, text="X", fg="red", command=lambda:
    setexpression("*"), height=4, width=8).grid(row=3, column=0,pady=10)
Button(root, text="/", fg="red", command=lambda:
    setexpression("/"), height=4, width=8).grid(row=4, column=0,pady=10)
Button(root, text="sqrt", fg="red", command= squart, height=4, width=8).grid(row=5, column=0, pady=10)
Button(root, text="1", fg="red", command=lambda:
    setexpression("1"), height=4, width=8).grid(row=1, column=1,pady=10)
Button(root, text="2", fg="red", command=lambda:
    setexpression("2"), height=4, width=8).grid(row=1, column=2,pady=10)
Button(root, text="3", fg="red", command=lambda:
    setexpression("3"), height=4, width=8).grid(row=1, column=3,pady=10)
Button(root, text="4", fg="red", command=lambda:
    setexpression("4"), height=4, width=8).grid(row=2, column=1,pady=10)
Button(root, text="5", fg="red", command=lambda:
    setexpression("5"), height=4, width=8).grid(row=2, column=2)
Button(root, text="6", fg="red", command=lambda:
    setexpression("6"), height=4, width=8).grid(row=2, column=3,pady=10)
Button(root, text="7", fg="red", command=lambda:
    setexpression("7"), height=4, width=8).grid(row=3, column=1,pady=10)
Button(root, text="8", fg="red", command=lambda:
    setexpression("8"), height=4, width=8).grid(row=3, column=2,pady=10)
Button(root, text="9", fg="red", command=lambda:
    setexpression("9"), height=4, width=8).grid(row=3, column=3,pady=10)
Button(root, text="0", fg="red", command=lambda:
    setexpression("0"), height=4, width=8).grid(row=4, column=2,pady=10)
Button(root, text=".", fg="red", command=lambda:
    setexpression("."), height=4, width=8).grid(row=4, column=1,pady=10)

# "=" button to call the calculator button which will return and
# show the calculated value in the entry widget
Button(root, text="=", fg="red", command=calculator, height=4,
       width=8).grid(row=4, column=3, pady=10)

# "Clear" button to call the clear function which will clear the
# entry widget so that the user can start clculating again
Button(root, text="Clear", fg="red", command=clear, height=4,
       width=20).grid(row=5, column=1, pady=10)


# .mainloop() is used when the code is ready to run
root.mainloop()