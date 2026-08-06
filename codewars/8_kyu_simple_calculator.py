"""
Simple calculator
https://www.codewars.com/kata/5810085c533d69f4980001cf

In this script your task is to create a function calculator that takes three arguments x, y and op.
The function should compute the operation and return the result.

If any argument is invalid (x or y are not numbers, or op is not one of '+', '-', '*', '/'),
the function should return the string 'unknown value'.

Examples:
calculator(1, 2, '+') == 3
calculator(5, 2, '*') == 10
calculator('a', 2, '+') == 'unknown value'

Fundamentals
"""

import operator


OPERATORS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


# 1. Dict of lambdas + type check with isinstance() and op membership check
def calculator(x: int | float, y: int | float, op: str):
    if isinstance(x, (int, float)) and isinstance(y, (int, float)) and op in OPERATORS:
        return OPERATORS[op](x, y)
    return 'unknown value'


# 2. Alternative — dict of operator module functions instead of lambdas
def calculator_operator_module(x: int | float, y: int | float, op: str):
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    if isinstance(x, (int, float)) and isinstance(y, (int, float)) and op in operators:
        return operators[op](x, y)
    return 'unknown value'
