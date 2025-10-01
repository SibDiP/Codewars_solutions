"""
6_kyu_Stop_gninnipS_My_sdroW.py

Codewars kata: Stop gninnipS My sdroW!
Level: 6 kyu
Link: https://www.codewars.com/kata/5264d2b162488dc400000001

Description:
Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (just like the name of this Kata).

- Strings passed in will consist of only letters and spaces.
- Spaces will be included only when more than one word is present.

Examples:
spin_words("Hey fellow warriors")  =>  "Hey wollef sroirraw" 
spin_words("This is a test")       =>  "This is a test"
spin_words("This is another test") =>  "This is rehtona test"

Solutions:
"""

# 1: generator, [::-1], len(), .split()
def spin_words(sentence):
    return ' '.join([
        word if len(word) < 5
        else word[::-1]
        for word in sentence.split()
    ])

# Alternative solutions for comparison:

# Solution 2: Traditional for loop approach
def spin_words_loop(sentence):
    words = sentence.split()
    result = []
    
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    
    return ' '.join(result)

# Solution 3 (AI): map(), lambda, .split()
def spin_words_map(sentence):
    return ' '.join(map(lambda word: word[::-1] if len(word) >= 5 else word, sentence.split()))

# Test cases
print(spin_words("Hey fellow warriors"))      # "Hey wollef sroirraw"
print(spin_words("This is a test"))           # "This is a test" 
print(spin_words("This is another test"))     # "This is rehtona test"
print(spin_words("You are almost to the last test"))  # "You are tsomla to the last test"
print(spin_words("Just kidding there is still one more"))  # "Just gniddik there is llits one more"
