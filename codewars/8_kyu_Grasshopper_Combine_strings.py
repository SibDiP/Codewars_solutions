# 8 kyu - Grasshopper - Combine strings
# https://www.codewars.com/kata/grasshopper-combine-strings
#
# Combine strings function - create a function named combine_names that accepts 
# two parameters (first_name and last_name) and returns a single string with 
# the two names combined with a space.
#
# f-строка, аннотации типов

def combine_names(name: str, surname: str) -> str:
    return f'{name} {surname}'