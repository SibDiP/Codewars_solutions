"""
6_kyu_Your_order,_please.py

Codewars kata: Your order, please
Level: 6 kyu
Link: https://www.codewars.com/kata/55c45be3b2079eccff00010f

Description:
Your task is to sort a given string. Each word in the string will contain 
a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the empty string is given, empty string should be returned.

Example:
"is2 Thi1s T4est 3a" --> "Thi1s is2 3a T4est"

Solutions:
"""

# Solution 1: split(), list comprehansion, for-loops, if, key-value in dict.items(), join()
def order(sentence):
    words = sentence.split()
    words_dict = {}
    # making placeholders
    result_list = ["" for i in range(len(words))]

    # serch for digit and keep them
    for word in words:
        for char in word:
            if char.isdigit():
                words_dict[word] = char
                break
    # ordering
    for key, value in words_dict.items():
        result_list[int(value)-1] = key

    # return
    return " ".join(result_list)

# Test cases
print(order("is2 Thi1s T4est 3a"))  # "Thi1s is2 3a T4est"
print(order("4of Fo1r pe6ople g3ood th5e the2"))  # "Fo1r the2 g3ood 4of th5e pe6ople"
print(order(""))  # ""
