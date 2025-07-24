"""
6_kyu_Who_likes_it.py

Description:

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
Strings
Fundamentals
"""

# 1. if-elif, .join()
def likes(names):
    result = ""
    names_len = len(names)
    
    if not names:
        result = "no one likes this"
    elif names_len == 1:
        result = "".join([names[0], " likes this" ])
    elif names_len == 2:
        result = "".join([names[0], " and ", names[1], " like this"])
    elif names_len == 3:
        result = "".join([names[0], ", ", names[1], " and ", names[2], " like this"])
    elif names_len > 3:
        others_num = len(names[2:])
        result = "".join([names[0], ", ", names[1], " and ", str(others_num), 
                          " others like this"])
        
    return result

# 2. (FC) dict, .format(), [:] | better looking, but worse efficiency
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)