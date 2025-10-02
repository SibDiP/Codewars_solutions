"""

7_kyu_Descending_Order.py

Codewars kata: Descending Order

Level: 7 kyu

Link: https://www.codewars.com/kata/5467e4d82edf8bbf40000155

Description:

Your task is to make a function that can take any non-negative integer as an argument 
and return it with its digits in descending order. Essentially, rearrange the digits 
to create the highest possible number.

Examples:

descending_order(42145) => 54421
descending_order(145263) => 654321
descending_order(123456789) => 987654321

"""

def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))

# Test cases
print(descending_order(42145))      # 54421
print(descending_order(145263))     # 654321
print(descending_order(123456789))  # 987654321
print(descending_order(0))          # 0
print(descending_order(1))          # 1