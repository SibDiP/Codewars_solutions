# 6 kyu - Cat and Mouse - Harder Version
# https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf
#
# You will be given a string (x) featuring a cat 'C', a mouse 'm' and a dog 'D'.
# The rest of the string will be made up of '.'.
# You need to find out if the cat can catch the mouse from its current position.
# The cat can jump at most j characters at a time.
#
# Rules:
# - If not all three characters are present → 'boring without all three'
# - If the distance between cat and mouse is greater than j → 'Escaped!'
# - If the dog is located between the cat and the mouse → 'Protected!'
# - Otherwise → 'Caught!'
#
# 1. Основное решение — ищем позиции 'C', 'm' и 'D' через str.find(),
#    проверяем наличие всех трёх, затем сравниваем расстояние с j
#    и проверяем, не находится ли собака между котом и мышью
#    (цепное сравнение min() < d_pos < max()).
# 2. Альтернатива — то же самое, но с отдельными проверками через
#    sorted() и явными условиями == -1.

def cat_mouse(x: str, j: int) -> str:
    # наличие всех трёх персонажей
    c_pos, m_pos, d_pos = x.find('C'), x.find('m'), x.find('D')
    if -1 in (c_pos, m_pos, d_pos):
        return 'boring without all three'

    # расстояние между котом и мышью
    if abs(c_pos - m_pos) > j:
        return 'Escaped!'

    # собака между котом и мышью
    if min(c_pos, m_pos) < d_pos < max(c_pos, m_pos):
        return 'Protected!'

    return "Caught!"


# Альтернативное решение — проверки разбиты на отдельные шаги
def cat_mouse_alternative(x: str, j: int) -> str:
    c_pos = x.find('C')
    m_pos = x.find('m')
    d_pos = x.find('D')
    if c_pos == -1 or m_pos == -1 or d_pos == -1:
        return 'boring without all three'
    if abs(c_pos - m_pos) > j:
        return 'Escaped!'
    left, right = sorted((c_pos, m_pos))
    if left < d_pos < right:
        return 'Protected!'
    return 'Caught!'
