"""
6_kyu_Give_me_a_Diamond.py

Codewars kata: Give me a Diamond
Level: 6 kyu
Link: https://www.codewars.com/kata/5503013e34137eeeaa001648/python

Description:
Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. 
Since James doesn't know how to make this happen, he needs your help.

Task:
You need to return a string that looks like a diamond shape when printed on the screen, 
using asterisk (*) characters. Trailing spaces should be removed, and every line must be 
terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible 
to print a diamond of even or negative size.

A size 3 diamond:
 *
***
 *

A size 5 diamond:
  *
 ***
*****
 ***
  *

Solutions:
"""

# 1. abs distance to diamond mid, .append(), join()
def diamond(n):   
    # if even or negative -> None
    if n <= 0 or n % 2 == 0:
        return None
    
    mid = n // 2
    lines = []
    
    for i in range(n):
        dist_to_mid = abs(mid - i)
        stars_amount = n - 2 * dist_to_mid
        spaces_amount = dist_to_mid
        
        lines.append(" " * spaces_amount + "*" * stars_amount + "\n")
    
    return "".join(lines)

# 2. (FC) nice&easy. Make mid and add similar lines from both sides
def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None
    
    result = "*" * n + "\n"
    spaces = 1
    n -= 2
    
    while n > 0:
        current = " " * spaces + "*" * n + "\n"
        spaces += 1
        n -= 2
        result = current + result + current
    
    return result.rstrip("\n")

# Test cases
print(diamond(3))
print(diamond(5))
print(diamond(2))  # None
print(diamond(-1))  # None
