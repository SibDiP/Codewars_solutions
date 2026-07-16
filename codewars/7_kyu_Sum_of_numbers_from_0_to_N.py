# 7 kyu - Sum of numbers from 0 to N
# https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763
#
# We want to generate a string that looks like:
#   "0+1+2+...+n = sum"
# Examples:
#   n = 5  → "0+1+2+3+4+5 = 15"
#   n = 0  → "0=0"
#   n = -5 → "-5<0"
#
# 1. Моё решение — компактное, с тернарным оператором для особых случаев
#    и использованием map(str, range(n+1)) для построения последовательности.
# 2. Альтернатива (более читаемая) — явные проверки условий через if/elif.

def show_sequence(n: int) -> str:
    # Основное решение — компактное, но тернарники могут быть сложнее для восприятия
    sequence = "+".join(map(str, range(n + 1)))
    total = (1 + n) * n // 2  # формула Гаусса для суммы 0..n
    
    return "0=0" if n == 0 else f"{n}<0" if n < 0 else f"{sequence} = {total}"


# Альтернативное решение — более читаемое, с явными условиями
def show_sequence_alternative(n: int) -> str:
    if n == 0:
        return "0=0"
    elif n < 0:
        return f"{n}<0"
    
    sequence = "+".join(map(str, range(n + 1)))
    total = (1 + n) * n // 2
    return f"{sequence} = {total}"