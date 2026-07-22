# 7 kyu - Professor Oak's Trouble - New Pokedex prototype
# https://www.codewars.com/kata/57520361f2dac757360018ce
#
# Professor Oak is building a new Pokedex prototype. Each Pokemon has a name, level, and type.
# The info() method should return a string like:
#   "Pikachu, a wet and fair Pokemon."
# where "wet" is an alias for the type (water→wet, fire→fiery, grass→grassy)
# and "fair" is the level grade based on breakpoints:
#   level < 20  → "weak"
#   20 ≤ level < 50 → "fair"
#   level ≥ 50 → "strong"
#
# 1. Моё решение — использует bisect_left для нахождения индекса в списке breakpoints.
# 2. Альтернатива (из комментариев) — использует булеву арифметику для вычисления индекса:
#    (level > 20) + (level > 50) даёт 0, 1 или 2.

from bisect import bisect_left

class PokeScan:
    LEVEL_BREAKPOINTS: tuple[int, ...] = (20, 50)
    LEVEL_GRADES: tuple[str, ...] = ('weak', 'fair', 'strong')
    PKMNTYPES_ALIAS: dict[str, str] = {
        'water': 'wet',
        'fire': 'fiery',
        'grass': 'grassy',
    }

    def __init__(self, name: str, level: int, pkmntype: str) -> None:
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self) -> str:
        # Основное решение — используем bisect_left для определения индекса
        level_word = PokeScan.LEVEL_GRADES[bisect_left(PokeScan.LEVEL_BREAKPOINTS, self.level)]
        pkmntype_word = PokeScan.PKMNTYPES_ALIAS.get(self.pkmntype, self.pkmntype)
        return f"{self.name}, a {pkmntype_word} and {level_word} Pokemon."


# Альтернативное решение — с булевой арифметикой (без импорта bisect)
class PokeScanAlternative:
    LEVEL_BREAKPOINTS: tuple[int, ...] = (20, 50)
    LEVEL_GRADES: tuple[str, ...] = ('weak', 'fair', 'strong')
    PKMNTYPES_ALIAS: dict[str, str] = {
        'water': 'wet',
        'fire': 'fiery',
        'grass': 'grassy',
    }

    def __init__(self, name: str, level: int, pkmntype: str) -> None:
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self) -> str:
        # Вычисляем индекс: результат сложения двух булевых значений (0,1,2)
        index = (self.level > PokeScan.LEVEL_BREAKPOINTS[0]) + (self.level > PokeScan.LEVEL_BREAKPOINTS[1])
        level_word = PokeScan.LEVEL_GRADES[index]
        pkmntype_word = PokeScan.PKMNTYPES_ALIAS.get(self.pkmntype, self.pkmntype)
        return f"{self.name}, a {pkmntype_word} and {level_word} Pokemon."