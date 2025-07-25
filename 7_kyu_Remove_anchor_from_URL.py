"""
Remove anchor from URL
https://www.codewars.com/kata/51f2b4448cadf20ed0000386

Description:

Complete the function/method so that it returns the url with anything after the anchor (#) removed.
Examples

"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"

Regular Expressions
Strings
Fundamentals
"""

def remove_url_anchor(url):
    return url.split("#")[0]