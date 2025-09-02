"""
7_kyu_Sum_of_the_first_nth_term_of_Series.py

Codewars kata: Sum of the first nth term of Series
Level: 7 kyu
Link: https://www.codewars.com/kata/555eded1ad94b00403000071

Description:
Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...

You will need to figure out the rule of the series to complete this.

Rules:
- You need to round the answer to 2 decimal places and return it as String.
- If the given value is 0 then it should return "0.00".
- You will only be given Natural Numbers as arguments.

Solutions:
"""

def series_sum(n):
    series = [1/(1 + i * 3) for i in range(n)]
    return f"{sum(series):.2f}"

# Test cases
print(series_sum(1))  # "1.00"
print(series_sum(2))  # "1.25"
print(series_sum(3))  # "1.39"
print(series_sum(0))  # "0.00"