# 7 kyu - Method For Counting Total Occurence Of Specific Digits
# https://www.codewars.com/kata/method-for-counting-total-occurence-of-specific-digits
#
# We need a method in class List that returns a list of tuples (digit, count) 
# for each digit in digits_list, counting total occurrences in the string 
# representation of all integers in integers_list (ignore negative sign).
#
# Генераторное выражение, метод str.count, list comprehension, abs()

class List(object):
    def count_spec_digits(
        self,
        integers_list: list[int],
        digits_list: list[int]
    ) -> list[tuple[int, int]]:
        
        all_digits = "".join(str(abs(x)) for x in integers_list)
        return [(d, all_digits.count(str(d))) for d in digits_list]