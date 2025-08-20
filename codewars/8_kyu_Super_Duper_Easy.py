"""
8 kyu Super Duper Easy

Description:
Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

Fundamentals
"""

def problem(a):
    result = None

    try:
        result = a * 50 + 6
    except TypeError:
        result = "Error"
    
    return result

