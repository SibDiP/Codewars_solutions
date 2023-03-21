# 1. dict, two for loops
def duplicate_count(text):
    lower_text = text.lower()
    symbols_dict = dict()
    duplicates_counter = 0

    for i in lower_text:
        symbols_dict[i] = symbols_dict.get(i, 0) + 1

    for v in symbols_dict.values():
        if v > 1:
            duplicates_counter += 1
    return duplicates_counter


# 2. iterator and set()
def duplicate_count(text):
    text_lower = text.lower()
    duplicate_counter = len(set(c for c in text_lower if text_lower.count(c) > 1))

    return duplicate_counter


# 3. (FC) for loop, seen and dupes sets (nice one)
def duplicate_count(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)
