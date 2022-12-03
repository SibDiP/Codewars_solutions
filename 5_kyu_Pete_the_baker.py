"""
5 kyu Pete, the baker
https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

Instruction: Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in
maths. Can you help him to find out, how many cakes he could bake considering his recipes? Write a function cakes(),
which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of
cakes Pete can bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of
sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:

# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

ALGORITHMS """


# 1. loop, try/except, min()

def cakes(recipe: dict, available: dict) -> int:
    cakes_counter = int

    for ingredient, amount in recipe.items():
        try:
            cakes_counter_current = (available.get(ingredient)) // amount
        except TypeError:  # ingredient isn't available at all
            return 0

        try:
            cakes_counter = min(cakes_counter, cakes_counter_current)
        except TypeError:
            cakes_counter = cakes_counter_current

        if cakes_counter <= 0:
            return 0

    return cakes_counter


"""
2. Oneliner with get() | from discussion
nice, but can't handle negative numbers
"""


# def cakes(recipe, available):
#     return min(available.get(k, 0) // recipe[k] for k in recipe)


# Test_zone
import pytest


@pytest.mark.parametrize('recipe, available, expected_amount', [
    ({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}, 2),
    ({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000},
     0)])
def test_examples(recipe, available, expected_amount):
    assert cakes(recipe, available) == expected_amount

def test_negative_amount_available():
    res = cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": -5, "milk": 200})
    assert res == 0
