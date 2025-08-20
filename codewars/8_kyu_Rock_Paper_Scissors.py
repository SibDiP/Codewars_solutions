'''8 kyu Rock Paper Scissors
https://www.codewars.com/kata/5672a98bdbdd995fad00000f/solutions/python

Rock Paper Scissors

Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"

Fundamentals
'''

# 1. if-elif-else construction, easy to read
def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors" or p1 == "paper" and p2 == "rock" or p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    else:
        return "Player 2 won!"