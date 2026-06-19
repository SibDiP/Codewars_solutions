"""
https://www.codewars.com/kata/55a144eff5124e546400005a

Classy Classes

Complete the Person class with:
- A constructor that takes name and age (both strings/integers).
- A property 'info' that returns a string in the format: "{name}s age is {age}".

Example:
person = Person("John", 34)
person.info => "Johns age is 34"
"""

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    @property
    def info(self) -> str:
        return f"{self.name}s age is {self.age}"
