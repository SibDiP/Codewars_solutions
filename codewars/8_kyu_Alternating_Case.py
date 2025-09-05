"""
8_kyu_altERnaTIng_cAsE_ALTerNAtiNG_CaSe.py

Codewars kata: altERnaTIng cAsE <=> ALTerNAtiNG CaSe
Level: 8 kyu
Link: https://www.codewars.com/kata/56efc695740d30f963000557

Description:
Define to_alternating_case (or toAlternatingCase or ToAlternatingCase in your selected language) 
such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase.

For example:
"hello world" -> "HELLO WORLD"
"HELLO WORLD" -> "hello world"  
"hello WORLD" -> "HELLO world"
"HeLLo WoRLD" -> "hEllO wOrld"
"12345" -> "12345" // Non-alphabetical characters are unaffected
"1a2b3c4d5e" -> "1A2B3C4D5E"

As usual, your function/method should be pure, i.e. it should not mutate the original string.

Solutions:
"""

# Solution 1: Generator expression with ternary operator
def to_alternating_case(string):
    return "".join((
        i.casefold() if i.isupper() else
        i.upper()
        for i in string
    ))

# Solution 2 (FC): Built-in swapcase method - most Pythonic
def to_alternating_case(string):
    return string.swapcase()

# Test cases
print(to_alternating_case("hello world"))     # "HELLO WORLD"
print(to_alternating_case("HELLO WORLD"))     # "hello world"
print(to_alternating_case("hello WORLD"))     # "HELLO world"
print(to_alternating_case("HeLLo WoRLD"))     # "hEllO wOrld"
print(to_alternating_case("12345"))           # "12345"
print(to_alternating_case("1a2b3c4d5e"))      # "1A2B3C4D5E"