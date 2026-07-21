# 7 kyu - The Barksdale Code
# https://www.codewars.com/kata/573d498eb90ccf20a000002a
#
# For those that haven't seen the show, the Barksdale Organization has a simple
# method for encoding telephone numbers exchanged via pagers:
# "Jump to the other side of the 5 on the keypad, and swap 5's and 0's."
#
# Encoding rules:
#   0 ↔ 5 (swap)
#   1 → 9, 2 → 8, 3 → 7, 4 → 6  (mirror around 5)
#   6 → 4, 7 → 3, 8 → 2, 9 → 1
#
# 1. Моё решение — использует map с lambda, где для каждой цифры:
#    - '5' → '0'
#    - '0' → '5'
#    - остальные → str(10 - int(d))
# 2. Альтернатива (из комментариев) — использует str.maketrans для создания
#    таблицы перевода и метод translate. Более читаемо и эффективно.

def decode(strng: str) -> str:
    # Основное решение — компактное, с map и lambda
    return "".join(map(lambda d: "0" if d == "5" else ("5" if d == "0" else str(10 - int(d))), strng))


# Альтернативное решение — с использованием таблицы перевода
def decode_alternative(string: str) -> str:
    original: str = "0123456789"
    code: str     = "5987604321"
    table: dict[int, int] = str.maketrans(original, code)
    return string.translate(table)