"""
6 Kyu Simple Encryption #1 - Alternating Split

Implement a pseudo-encryption algorithm which given a string S and an integer 
N concatenates all the odd-indexed characters of S with all the even-indexed 
characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"

Together with the encryption function, you should also implement a 
decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, 
return the first argument without changes.

This kata is part of the Simple Encryption Series:

    Simple Encryption #1 - Alternating Split
    Simple Encryption #2 - Index-Difference
    Simple Encryption #3 - Turn The Bits Around
    Simple Encryption #4 - Qwerty

Have fun coding it and please don't forget to vote and rank this kata! :-)
Cryptography
Algorithms
Strings
Arrays
Fundamentals
"""
# 1. slice [:], for-loop, % 2. OK, but can be better
def decrypt(encrypted_text, n):
    try:
        text_len = len(encrypted_text)
    except TypeError:
        return encrypted_text

    temp_text = encrypted_text

    for iteration in range(n):
        split_index = text_len // 2
        odd = temp_text[:split_index]
        even = temp_text[split_index:]
        temp_text = ""
        
        for i in range(len(even)):
            temp_text = temp_text + even[i]
            try:
                temp_text = temp_text + odd[i]
            except IndexError:
                pass

    return temp_text

def encrypt(text: str, n: int) -> str:
    temp_text = text
    odd_indexed = ""
    even_indexed = ""
       
    for iteration in range(n):
        for i,v in enumerate(temp_text):
            if i % 2 == 1:
                odd_indexed = "".join((odd_indexed, v))
            else:
                even_indexed = "".join((even_indexed, v))
        
        temp_text = "".join((odd_indexed, even_indexed))
        odd_indexed, even_indexed = "", ""
        
    return temp_text


# 2. (FC) Advanced slicing and multiple assigment

def decrypt(s, n):
    if not s: return s
    o, l = len(s) // 2, list(s)
    for _ in range(n):
        l[1::2], l[::2] = l[:o], l[o:]
    return ''.join(l)


def encrypt(s, n):
    if not s: return s
    for _ in range(n):
        s = s[1::2] + s[::2]
    return s