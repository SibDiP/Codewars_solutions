# 8 kyu - Formatting decimal places #0
# https://www.codewars.com/kata/5641a03210e973055a00000d
#
# Each number should be formatted to two decimal places. 
# You don't need to check whether the input is a valid number because 
# only valid numbers are used in the tests.
#
# 1. Мой вариант: использует встроенный round(), но это банковское округление
#    (к ближайшему чётному), что может дать неожиданные результаты для .5.
# 2. Альтернатива (FC): Decimal с ROUND_HALF_UP — математическое округление,
#    более предсказуемое для финансовых расчётов.

def two_decimal_places(n):
    # Основное решение (простое, но с банковским округлением)
    return round(n, 2)


# Альтернативный вариант (из комментариев) — использует Decimal для точного
# округления "вверх от половины" (ROUND_HALF_UP), что соответствует
# математическому ожиданию.
from decimal import Decimal, ROUND_HALF_UP

def two_decimal_places_alternative(n):
    dn = Decimal(str(n)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
    return float(dn)