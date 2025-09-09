"""
5_kyu_Directions_Reduction.py

Codewars kata: Directions Reduction
Level: 5 kyu
Link: https://www.codewars.com/kata/550f22f4d758534c1100025a

Description:
A man was given directions to go from one point to another. The directions were "NORTH", "SOUTH", "WEST", "EAST".
Clearly "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too. Going in one direction and coming back the opposite
direction right away is a needless effort. Since this is the wild west, with dreadful weather and not much water,
it's important to save yourself some energy, otherwise you might die of thirst!

How I crossed a mountainous desert the smart way.

The directions given to the man are, for example, the following (depending on the language):
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable, better stay to the same place!
So the task is to give to the man a simplified version of the plan. A better plan in this case is:
["WEST"]

or
["WEST"] in C.

Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed.

Examples:
dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) => ["WEST"]
dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "SOUTH", "EAST"]) => ["NORTH", "WEST", "SOUTH", "EAST"]

Solutions:
"""

def dir_reduc(arr: list) -> list:
    OPPOSITE_DIRECTIONS_DICT = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST",
    }
    stack = []
    
    for direction in arr:
        if stack and OPPOSITE_DIRECTIONS_DICT[direction] == stack[-1]:
            stack.pop()
        else:
            stack.append(direction)
    
    return stack

# Test cases
print(dir_reduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))  
# ["WEST"]

print(dir_reduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "SOUTH", "EAST"])) 
# ["NORTH", "WEST", "SOUTH", "EAST"]

print(dir_reduc(["NORTH", "WEST", "SOUTH", "EAST"]))  
# ["NORTH", "WEST", "SOUTH", "EAST"]

print(dir_reduc(["NORTH", "SOUTH"]))  
# []