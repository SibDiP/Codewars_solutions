"""7 kyu Get the Middle Character
https://www.codewars.com/kata/56747fd5cb988479af000028/solutions/python

You are going to be given a word. Your job is to return the middle character of the word. If the word's length is
odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"

#Input

A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to
an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to
worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.
Fundamentals
Strings"""


# 1. if-elif-else, slice
def get_middle(s):
    s_len = len(s)

    if s_len == 1:
        return s
    elif s_len % 2 == 0:
        mid_ind = round(s_len / 2) - 1
        return f'{s[mid_ind:mid_ind + 2]}'
    else:
        return s[round(s_len // 2)]


# 2. (FC) divmod(), if-else oneliner, slice [muc better than 1]
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
