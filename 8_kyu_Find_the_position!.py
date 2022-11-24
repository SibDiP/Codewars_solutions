"""Find the position!
https://www.codewars.com/kata/5808e2006b65bff35500008f/solutions/python
DESCRIPTION:
When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

#FUNDAMENTALS"""

# My first solution
def position(alphabet): return f"""Position of alphabet: {'abcdefghijklmnopqrstuvwxyz'.find(alphabet.lower())+1}"""

print(position('C'))

# Solution with ascii

def position(alphabet): return f"""Position of alphabet: {ord(alphabet.lower()) - 96}"""

print(position('C'))