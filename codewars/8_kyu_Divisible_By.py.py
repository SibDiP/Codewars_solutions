# 8 kyu - Divisible By
# https://www.codewars.com/kata/55edaba99da3a9c84000003b
#
# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
# First argument is an array of numbers and the second is the divisor.
#
# list comprehension, filter, lambda

def divisible_by(numbers, divisor):
    # Основное решение (рекомендуемое) — list comprehension, читаемо и эффективно
    return [num for num in numbers if num % divisor == 0]

# Альтернативное решение из комментариев (менее читаемо и немного медленнее из-за lambda)
def divisible_by_alternative(numbers, divisor):
    return list(filter(lambda x: not x % divisor, numbers))