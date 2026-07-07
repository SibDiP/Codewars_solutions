# 7 kyu - Formatting decimal places #1
# https://www.codewars.com/kata/5641c3f809bf31f008000042
#
# The goal of this kata is to return a number with two decimal places,
# but **without rounding**. The number should be truncated (not rounded)
# to two decimal places.
# Example: 5.5589 → 5.55 (not 5.56)
#
# 1. Моё решение: использует Decimal с ROUND_DOWN для точного усечения,
#    что гарантирует корректную работу даже с числами с плавающей точкой.
# 2. Альтернатива (FC) - из комментариев: умножает на 100, приводит к int
#    (отбрасывая дробную часть) и делит на 100. Проще, но может дать
#    неожиданные результаты для отрицательных чисел (т.к. int(-2.5) = -2,
#    что даст -0.02 вместо -0.03, если бы было округление, но здесь усечение
#    идёт в сторону нуля, что соответствует ROUND_DOWN).

from decimal import Decimal, ROUND_DOWN

def two_decimal_places(number: float) -> float:
    # Основное решение с Decimal для точного усечения
    num = Decimal(str(number))
    result = num.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
    return float(result)


# Альтернативное решение (из комментариев) — усечение через умножение и int
def two_decimal_places_alternative(number: float) -> float:
    return int(number * 100) / 100.0