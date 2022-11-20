# Moving Zeros To The End
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/python

# Instructions:
# Write an algorithm that takes an array and moves all the zeros to the end, preserving the order of
# the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

# My solution:
def move_zeros(lst):
    for num in range(len(lst)):
        try:
            zero_index = lst.index(0)
        except ValueError:
            return lst

        lst.pop(zero_index)
        lst.append(0)

    return lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))


# Interesting solution:

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and type(x) is not bool)


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

# Explanation from comments:
# To explain a little: sorted() will sort an iterable of inputs (in this case, array),
# by whatever metric you define. If you gave it a list of ints and didn't tell it how to sort, it would sort them as
# you'd expect - the smallest first.
#
# However, you can tell sorted() what you want to sort by, with the key argument. key must be a function that returns
# something orderable.
#
# In this case, our function to sort by is a lambda function, which is just a shorthand way of writing a function
# inline. What does this function do? It returns True if x==0 and type(x) is not bool. So, all your 0s and 0.0s (and
# complex 0i + 0js? I don't know about those enough) will return True, while everything else - any non-zero int,
# or any str will return False. Also, False will return False, because even though False == 0, type(False) is bool.
#
# Alright, so we've got a bunch of True/False values as our key outputs... how the heck does the rest of this work?!
#
# Well, now we sort by the keys. Since False is equivalent to 0 and True is equivalent to 1, we put all of our False
# before all of our True. This means we put all of our (int, or str, or False) before all of our (0 or 0.0 or 0i + 0j).
#
# Ok, fine, but how come it doesn't screw up the order of things? If I sort (3, 2, 1) by their keys (True, True,
# True) why do I get (3, 2, 1) back out? Because Python's sort is a stable sort. That means, if two items compare
# equal, the first one in is the first one out. So, everything that gets a False stays in order, and everything that
# was True (aka 0-ish) stays in order; but all the False come before all the Truth.
#
# This solution is exceedingly clever... but not AT ALL best practice. I've glossed over a bunch of details,
# and it requires you to know things like Python uses stable sort and the only falsey values this function wants to
# keep "in place" is False... it would be really difficult to maintain/understand this code without a solid Python
# background, or a ton of comments.
