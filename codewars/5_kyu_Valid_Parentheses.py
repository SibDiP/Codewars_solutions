"""5 kyu Valid Parentheses
https://www.codewars.com/kata/52774a314c2333f0a7000688/solutions/python

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
Algorithms
"""
# 1. Two counters algorithm
def valid_parentheses(string):
    open_p_counter = 0
    close_p_counter = 0

    for i in range(len(string)):
        if string[i] == '(':
            open_p_counter += 1
        elif string[i] == ')':
            close_p_counter += 1

        if close_p_counter > open_p_counter:
            return False

    if open_p_counter == close_p_counter:
        return True
    else:
        return False

# 2 (FC) One counter realisation (much cleaner):
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
