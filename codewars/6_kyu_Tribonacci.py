"""
6_kyu_Tribonacci.py

Codewars kata: Tribonacci Sequence
Level: 6 kyu
Link: https://www.codewars.com/kata/556deca17c58da83c00002db

Description:
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting seed, we have:
[1, 1, 1, 3, 5, 9, 17, 31, ...]

But what if we started with [0, 0, 1] as a seed? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Solutions:
"""

#1. for-loop, condition checks for n, sum() slice
def tribonacci(signature, n):
    signature_len = len(signature)
    
    if n == 0:
        return []
    elif n < signature_len:
        return signature[:n]
    else:
        tribonachi_sequence = signature[:]
        
        for i in range(signature_len, n):
            new_num = sum(tribonachi_sequence[i-signature_len:i])
            tribonachi_sequence.append(new_num)

        return tribonachi_sequence[:n]

# 2. (FC) short loop with res[-3:]|
def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): 
        res.append(sum(res[-3:]))
    return res

# Test cases
print(tribonacci([1, 1, 1], 10))  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10))  # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
print(tribonacci([1, 0, 0], 10))  # [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
