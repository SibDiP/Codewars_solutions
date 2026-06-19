"""
https://www.codewars.com/kata/55805ab490c73741b7000064

makeBackronym

A backronym is an acronym formed from an already existing word by expanding
its letters into a phrase. For example, "code" -> "Confidence Over Data Experts".
You are given a preloaded dictionary where keys are uppercase letters and values
are corresponding words. Write a function make_backronym(acronym) that returns
the backronym as a string, with each word separated by a space.

Example (using a given dictionary):
make_backronym("code") => "Confidence Over Data Experts"
"""

# preloaded variable: "dictionary"

def make_backronym(acronym):
    return " ".join(dictionary[letter] for letter in acronym.upper())
