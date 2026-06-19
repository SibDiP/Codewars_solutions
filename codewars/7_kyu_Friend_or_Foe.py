"""
https://www.codewars.com/kata/55b42574ff091733d900002f

Friend or Foe?

Make a program that filters a list of strings and returns a list with only your friends.
A friend is someone whose name has exactly 4 letters.

Example:
friend(["Ryan", "Kieran", "Mark", "Jimmy"]) => ["Ryan", "Mark"]
"""

def friend(names: list) -> list:
    return [name for name in names if len(name) == 4]
