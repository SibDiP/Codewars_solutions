# 8 kyu - Grasshopper - Terminal Game #1
# https://www.codewars.com/kata/grasshopper-terminal-game-number-1/train/python
#
# Terminal Game - Create Hero Prototype
# In this first kata in the series, you need to define a Hero prototype to be used in a terminal game.
# The hero should have the following attributes:
#   name       | user argument or 'Hero'
#   position   | '00'
#   health     | 100
#   damage     | 5
#   experience | 0
#
# ООП, @dataclass, поля со значениями по умолчанию

from dataclasses import dataclass

@dataclass
class Hero:
    name: str = "Hero"
    position: str = "00"
    health: int = 100
    damage: int = 5
    experience: int = 0