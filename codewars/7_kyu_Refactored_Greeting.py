"""
7_kyu_Refactored_Greeting.py

Codewars kata: Refactored Greeting
Level: 7 kyu
Link: https://www.codewars.com/kata/5121303128ef4b495f000001

Description:
The following code could use a bit of object-oriented artistry. 
While it's a simple method and works just fine as it is, in a larger system it's best to organize 
methods into classes/objects. (Or, at minimum, retrieve the method into a module.)

You need to implement a Person class with a greet method.

The greet method should take a parameter other_name and return a string in the format:
"Hello {other_name}, my name is {self.name}"

Solutions:
"""

class Person:
    def __init__(self, name: str):
        self.name = name
    
    def greet(self, other_name: str) -> str:
        return f"Hello {other_name}, my name is {self.name}"

# Test cases
person = Person("John")
print(person.greet("Kate"))    # "Hello Kate, my name is John"
print(person.greet("Daniel"))  # "Hello Daniel, my name is John"

person2 = Person("Alice") 
print(person2.greet("Bob"))    # "Hello Bob, my name is Alice"