"""
8_kyu_Get_Planet_Name_By_ID.py

Codewars kata: Get Planet Name By ID
Level: 8 kyu
Link: https://www.codewars.com/kata/515e188a311df01cba000003

Description:
The function is not returning the correct values. Can you figure out why?

getPlanetName(3) // should return "Earth"

You need to fix the function to return the correct planet name based on the ID:
1 - Mercury
2 - Venus  
3 - Earth
4 - Mars
5 - Jupiter
6 - Saturn
7 - Uranus
8 - Neptune

Solutions:
"""

def get_planet_name(id):
    switch = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus", 
        8: "Neptune",
    }
    return switch.get(id, None)

# Test cases
print(get_planet_name(2))  # "Venus"
print(get_planet_name(5))  # "Jupiter"
print(get_planet_name(3))  # "Earth"
print(get_planet_name(4))  # "Mars"
print(get_planet_name(8))  # "Neptune"
print(get_planet_name(1))  # "Mercury"
