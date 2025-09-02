"""
8_kyu_Keep_up_the_hoop.py

Codewars kata: Keep up the hoop
Level: 8 kyu
Link: https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145

Description:
Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him.

Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message:
- If Alex gets 10 or more hoops, return the string "Great, now move on to tricks".
- If he gets less than 10 hoops, return the string "Keep at it until you get it".

Solutions:
"""

def hoop_count(n):
    PHRASES = ("Great, now move on to tricks",
              "Keep at it until you get it")
    return PHRASES[n<10]

def hoop_count(n):
    PHRASES = ("Great, now move on to tricks",
              "Keep at it until you get it")
    return PHRASES[0] if n >= 10 else PHRASES[1]

def hoop_count(n):
    return 'Great, now move on to tricks' if n >= 10 else 'Keep at it until you get it'

# Test cases
print(hoop_count(3))   # "Keep at it until you get it"
print(hoop_count(11))  # "Great, now move on to tricks"
print(hoop_count(10))  # "Great, now move on to tricks"