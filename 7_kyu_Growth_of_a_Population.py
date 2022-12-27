# 1. while loop, round down by //
def nb_year(p0, percent, aug, p):
    years_to_grow_counter = 0
    percentage = percent / 100

    while p0 < p:
        p0 = p0 + p0 * percentage // 1 + aug
        years_to_grow_counter += 1

    return years_to_grow_counter

# 2. (FC) addition argument, no round
def nb_year(p0, percent, aug, p, n = 0):
    while p > p0:
        p0 += p0*percent/100 + aug
        n += 1
    return n
