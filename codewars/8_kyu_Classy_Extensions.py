"""
https://www.codewars.com/kata/55a14aa4817efe41c20000bc

Classy Extensions

You need to complete the Cat class which extends Animal (preloaded).
The Cat class should have a speak() method that returns the cat's name followed by " meows.".
For example, if the cat's name is "Mr. Whiskers", speak() should return "Mr. Whiskers meows.".
"""

from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows."
