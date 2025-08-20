"""6 kyu Break camelCase
https://www.codewars.com/kata/5208f99aee097e6552000148/solutions/python

Complete the solution so that the function will break up camel casing, using a space between words.
Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

Strings
Fundamentals

"""
# 1. RegEx
import re

def solution(s):
    words = re.findall('[a-z][^A-Z]*|[A-Z][^A-Z]*', s)
    return " ".join(words)

# 2. (FC) RegEx, re.sub()
# r' \1' is a regular expression replacement string that inserts a space character followed
# by the contents of the first capturing group in the matched pattern. The r before the replacement string indicates
# that it is a raw string.
import re

def solution(s):
    return re.sub('([A-Z])', r' \1', s)