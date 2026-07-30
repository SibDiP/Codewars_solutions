"""
Bumps in the Road
https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python

Your car is old, it breaks down easily. The shock absorbers are gone and you think it can handle about 15 bumps
in a road before it dies completely.

Unfortunately for you, your car is very sensitive — if the road contains more than 15 bumps (character 'n'),
your car will be dead. Otherwise, it will be "Woohoo!".

Strings
Fundamentals
"""


# 1. One-liner using str.count(), ternary conditional
def bumps(road):
    return "Car Dead" if road.count('n') > 15 else "Woohoo!"
