# 8 kyu - No zeros for heroes
# https://www.codewars.com/kata/570a6a46455d08ff8d001002
#
# Numbers ending with zeros are boring. Get rid of them. Only the ending ones.
# Example: 1450 → 145, 960000 → 96, 1050 → 105
# If the number is 0, return 0.
#
# 1. Моё решение — преобразуем в строку, удаляем trailing zeros через rstrip('0'),
#    затем обратно в int. Обработка нуля через тернарный оператор.
# 2. Математическое решение (АИ + комментарии) — пока число делится на 10 без остатка,
#    делим его на 10. Более эффективно для больших чисел, без преобразований в строку.

def no_boring_zeros(n: int) -> int:
    # Основное решение — строковое, простое и читаемое
    return int(str(n).rstrip('0')) if n else 0


# Альтернативное решение — математическое, без преобразований в строку
def no_boring_zeros_alternative(n: int) -> int:
    if n == 0:
        return 0
    while n % 10 == 0:
        n //= 10
    return n