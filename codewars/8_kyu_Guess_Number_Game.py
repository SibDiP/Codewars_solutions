"""
8_kyu_Finish_Guess_the_Number_Game.py

Codewars kata: Finish Guess the Number Game
Level: 8 kyu
Link: https://www.codewars.com/kata/568018a64f35f0c613000054

Description:
Imagine you are creating a game where the user has to guess the correct number. 
But there is a limit of how many guesses the user can do.

If the user tries to guess more than the limit, it will throw an error saying "Guess limit exceeded!".
If the guess is the right number, it will return true.
If the guess is wrong, it will return false and a life will be deducted.

Can you finish the game?

You need to complete the class "Guesser" with the method "guess".

Solutions:
"""

class Guesser:
    def __init__(self, number: int, lives: int):
        self.number = number
        self.lives = lives

    def guess(self, n: int) -> bool:
        if self.lives == 0:
            raise ValueError("No lives left!")
        if n == self.number:
            return True
        else:
            self.lives -= 1
            return False

# Test cases
guesser = Guesser(10, 2)
print(guesser.guess(10))  # True
print(guesser.guess(15))  # False
print(guesser.guess(20))  # False

try:
    print(guesser.guess(25))  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")  # Error: No lives left!