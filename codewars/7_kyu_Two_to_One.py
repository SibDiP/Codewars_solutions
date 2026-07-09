# 7 kyu - Two to One
# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
#
# Take two strings a1 and a2, containing only letters from a to z.
# Return a new string of distinct letters, sorted alphabetically,
# that are present in either a1 or a2.
# Example: a1 = "xyaabbbccccdefww", a2 = "xxxxyyyyabklmopq"
#          → "abcdefklmopqwxy"
#
# 1. Моё решение — объединяем строки, создаём множество (удаляем дубли),
#    сортируем и объединяем в строку.
# 2. Альтернатива (big data) — создаём множества для каждой строки
#    и объединяем их через оператор | (union).

def longest(a1: str, a2: str) -> str:
    # Основное решение — простое и читаемое
    return "".join(sorted(set(a1 + a2)))


# Альтернативное решение (для больших данных — более явное объединение множеств)
def longest_alternative(a1: str, a2: str) -> str:
    return "".join(sorted(set(a1) | set(a2)))