# 7 kyu - Number of People in the Bus
# https://www.codewars.com/kata/5648b12ce68d9daa6b000099
#
# There is a bus moving in the city, and it takes and drops some people at each bus stop.
# You are given a list of pairs (number of people getting on, number getting off).
# The task is to return the number of people remaining on the bus after the last stop.
# (The bus starts empty, and the number of people never goes negative.)
#
# 1. Моё решение (итеративное) — аккумулируем входящих и выходящих отдельно.
# 2. Альтернатива (из комментариев) — генераторное выражение с суммой разностей,
#    более компактно, но может быть менее читаемо для новичков.

def number(bus_stops: list[list[int]]) -> int:
    # Основное решение — явное сложение в цикле
    get_on = 0
    get_out = 0
    
    for stop in bus_stops:
        get_on += stop[0]
        get_out += stop[1]
    
    return get_on - get_out


# Альтернативное решение (более компактное, на генераторе)
def number_alternative(bus_stops: list[list[int]]) -> int:
    return sum(on - out for on, out in bus_stops)