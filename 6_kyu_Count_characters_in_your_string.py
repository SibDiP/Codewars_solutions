"""6 kyu Count characters in your string
https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
Strings
Fundamentals


"""

# Var 1. | for-loop, if-else
def count(s):
    char_counter_dict = {}

    for char in s:
        if char in char_counter_dict:
            char_counter_dict[char] += 1
        else:
            char_counter_dict[char] = 1

    return char_counter_dict

# Var 2. (FC) | for-loop, dict.get(value, default)
def count(s):
  char_counter_dict = {}

  for char in s:
    char_counter_dict[char] = char_counter_dict.get(char, 0) + 1

  return char_counter_dict