"""
8_kyu_Powers_of_2.py

Codewars kata: Powers of 2
Level: 8 kyu
Link: https://www.codewars.com/kata/57a083a57cb1f31db7000028

Description:
Complete the function that takes a non-negative integer n as input, 
and returns a list of all the powers of 2 with the exponent ranging from 0 to n (inclusive).

For example:
n = 0  ==> [1]        # [2^0]
n = 1  ==> [1, 2]     # [2^0, 2^1] 
n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

Solutions:
"""

def powers_of_two(n): 
    return [2 ** i for i in range(n+1)]

# Test cases
print(powers_of_two(0))  # [1]
print(powers_of_two(1))  # [1, 2]
print(powers_of_two(2))  # [1, 2, 4]
print(powers_of_two(4))  # [1, 2, 4, 8, 16]