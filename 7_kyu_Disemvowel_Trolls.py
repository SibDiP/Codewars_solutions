"""7_kyu_Disemvowel_Trolls
https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
Strings
Regular Expressions
Fundamentals

"""
# 1. (FC) | ''.join(), list comprehansion
def disemvowel(string_):
    vowels = "AaEeIiOoUu"

    return ''.join(char for char in string_ if char not in vowels)

# 2. (FC) | re, re.sub()
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)