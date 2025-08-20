"""
6_kyu_Consecutive_strings.py

Codewars kata: Consecutive strings
Level: 6 kyu
Link: https://www.codewars.com/kata/56a5d994ac971f1ac500003e

Описание задачи:
Дан массив строк strarr и число k. Необходимо вернуть первую самую длинную строку, полученную
склеиванием k последовательных строк из массива.

Решения пользователя:

#1. Использование max() с генератором и ''.join

def longest_consec(strarr: list, k: int) -> str:
    if k <= 0 or k > len(strarr):
        return ""
    
    return max((''.join(strarr[i:i+k]) for i in range(len(strarr) - k + 1)), key=len)

#2. Два вложенных цикла и max() с key=len

def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""  

    longest_str = ""

    for i in range(len(strarr) - k + 1):
        current_str = ""
        for j in range(k):
            current_str += strarr[i + j]  
            
        longest_str = max(longest_str, current_str, key=len)  

    return longest_str

# Примеры использования
print(longest_consec(["zone","abigail","theta","form","libe","zas","theta","abigail"], 2))  # "abigailtheta"
print(longest_consec([], 3))  # ""