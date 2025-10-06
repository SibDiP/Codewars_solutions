"""
8_kyu_Name_Your_Python.py

Codewars kata: Name Your Python!
Level: 8 kyu
Link: https://www.codewars.com/kata/53cf459503f9bbb774000003

Description:
Define a class Python with a constructor that takes one argument (name) and assigns it to instance property `name`.

Examples:
py = Python("Monty")
print(py.name)  # "Monty"

Solutions:
"""

class Python:
    def __init__(self, name):
        self.name = name

# Test cases
py = Python("Monty")
print(py.name)  # "Monty"
py2 = Python("Guido")
print(py2.name) # "Guido"