"""Cat years, Dog years
https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/solutions/python

Kata Task

I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

    humanYears >= 1
    humanYears are whole numbers only

Cat Years

    15 cat years for first year
    +9 cat years for second year
    +4 cat years for each year after that

Dog Years

    15 dog years for first year
    +9 dog years for second year
    +5 dog years for each year after that

References

    http://www.catster.com/cats-101/calculate-cat-age-in-cat-years
    http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html

If you liked this Kata there is another related one here
Fundamentals
"""

# 1. if * 3
def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0

    if human_years >= 1:
        cat_years += 15
        dog_years += 15
    if human_years >= 2:
        cat_years += 9
        dog_years += 9
    if human_years > 2:
        addition_years = human_years - 2
        cat_years += addition_years * 4
        dog_years += addition_years * 5

    return [human_years, cat_years, dog_years]


# 2. (FC) multiplication with booleans (clever!)

def human_years_cat_years_dog_years(n):
    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))
    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))
    return [n, cat_years, dog_years]