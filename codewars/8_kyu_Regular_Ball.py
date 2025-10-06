"""
8_kyu_Regular_Ball_Super_Ball.py

Codewars kata: Regular Ball Super Ball
Level: 8 kyu
Link: https://www.codewars.com/kata/53f0f358b9cb376eca001079

Description:
Write a class Ball that accepts one argument for constructor (ball type) and assigns it to instance property.
If no argument is given, ball type should be "regular" by default.

Examples:
ball1 = Ball()
print(ball1.ball_type)   # "regular"

ball2 = Ball("super")
print(ball2.ball_type)   # "super"

Solutions:
"""

class Ball(object):
    def __init__(self, ball_type: str = 'regular'):
        self.ball_type = ball_type

# Test cases
ball1 = Ball()
print(ball1.ball_type)   # "regular"

ball2 = Ball("super")
print(ball2.ball_type)   # "super"
