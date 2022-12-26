"""7 kyu Exes and Ohs
Description:
Check to see if a string has the same amount of 'x's and
'o's. The method must return a boolean and be case insensitive.
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

Fundamentals
"""


# 1. if-else oneliner, count(), lower()
def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') else False

# 2. (from comments) Oh..ofcourse... There's no need in if-else

def xo2(s):
    return s.lower().count('x') == s.lower().count('o')

# 3. more readable version
def xo3(s):
    s = s.lower()
    return s.count('x') == s.count('o')

# test zone
import pytest


@pytest.mark.parametrize('s, expected_result', [('xo', True),
                                                ('xo0', True),
                                                ('xxxoo', False)])
def test_example(s, expected_result):
    assert xo(s) == expected_result
