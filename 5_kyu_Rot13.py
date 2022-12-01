""" 5 kyu Rot13
https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

Discription:
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 
13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be 
returned as they are. Only letters from the latin/english alphabet should be shifted, 
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

CIPHERS FUNDAMENTALS
"""

# Solution wits ord() and ASCII
def rot13(message):
    rot13_message = ''
    for i in message:
        if i.isalpha():
            i_ascii = ord(i)
            if i.isupper():
                if i_ascii + 13 > 90:
                    i_ascii = 64 + (i_ascii + 13 - 90)
                else:
                    i_ascii += 13
            else:
                if i_ascii + 13 > 122:
                    i_ascii = 96 + (i_ascii + 13 - 122)
                else:
                    i_ascii += 13
        else:
            rot13_message += i
            continue
        rot13_message += chr(i_ascii)
    return rot13_message

print(rot13("Test"))


# Cool variant with translate() and maketrans()

def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

