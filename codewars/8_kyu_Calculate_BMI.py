"""
8_kyu_Calculate_BMI.py
https://www.codewars.com/kata/57a429e253ba3381850000fb

Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
Fundamentals
"""
#1 Tuple() insead of list[] for efficiency. One return statement instead of 4.
def bmi(weight, height):
    return_options = ("Underweight", "Normal", "Overweight", "Obese")
    return_index = float
    
    bmi = weight / height ** 2
    
    if bmi <= 18.5:
        return_index = 0
    elif bmi <= 25.0:
        return_index = 1
    elif bmi <= 30.0:
        return_index = 2
    elif bmi > 30.0:
        return_index = 3
    
    return return_options[return_index]