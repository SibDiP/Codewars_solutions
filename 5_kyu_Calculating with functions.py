"""5_kyu_Calculating_with_Functions
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

Instructions:

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

    seven(times(five())) # must return 35
    four(plus(nine())) # must return 13
    eight(minus(three())) # must return 5
    six(divided_by(two())) # must return 3

Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
"""

# First try. Learn about nonlocal and global variables in functions

def zero(inner=None):
    if inner is None:
        global num2
        num2 = 0
    elif inner:
        global num1
        num1 = 0
        return operator_switch(inner)


def one(inner=None):
    if inner is None:
        global num2
        num2 = 1
    elif inner:
        global num1
        num1 = 1
        return operator_switch(inner)


def two(inner=None):
    if inner is None:
        global num2
        num2 = 2
    elif inner:
        global num1
        num1 = 2
        return operator_switch(inner)


def three(inner=None):
    if inner is None:
        global num2
        num2 = 3
    elif inner:
        global num1
        num1 = 3
        return operator_switch(inner)


def four(inner=None):
    if inner is None:
        global num2
        num2 = 4
    elif inner:
        global num1
        num1 = 4
        return operator_switch(inner)


def five(inner=None):
    if inner is None:
        global num2
        num2 = 5
    elif inner:
        global num1
        num1 = 5
        return operator_switch(inner)


def six(inner=None):
    if inner is None:
        global num2
        num2 = 6
    elif inner:
        global num1
        num1 = 6
        return operator_switch(inner)


def seven(inner=None):
    if inner is None:
        global num2
        num2 = 7
    elif inner:
        global num1
        num1 = 7
        return operator_switch(inner)


def eight(inner=None):
    if inner is None:
        global num2
        num2 = 8
    elif inner:
        global num1
        num1 = 8
        return operator_switch(inner)


def nine(inner=None):
    if inner is None:
        global num2
        num2 = 9
    elif inner:
        global num1
        num1 = 9
        return operator_switch(inner)


def plus(num1=int, num2=None):
    if num2 is None:
        return 'plus'
    else:
        return num1 + num2


def minus(num1=int, num2=None):
    if num2 is None:
        return 'minus'
    else:
        return num1 - num2


def times(num1=int, num2=None):
    if num2 is None:
        return 'times'
    else:
        return num1 * num2


def divided_by(num1=int, num2=None):
    if num2 is None:
        return 'divided_by'
    else:
        return int(num1 // num2)


def operator_switch(operator):
    if operator == 'times':
        return times(num1, num2)
    elif operator == 'plus':
        return plus(num1, num2)
    elif operator == 'minus':
        return minus(num1, num2)
    elif operator == 'divided_by':
        return divided_by(num1, num2)


print(seven(minus(zero())))
print(four(plus(nine())))
print(six(divided_by(two())))
