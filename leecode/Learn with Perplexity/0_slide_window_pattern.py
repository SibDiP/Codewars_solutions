### Slide Window pattern. Study. 

def max_sum_window_len(arr: list[int], K: int) -> int:
    left = 0
    current_sum = 0
    best = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > K:
            current_sum -= arr[left]
            left += 1
        
        best = max(best, right - left + 1)
    
    return best

num_list = [2, 1, 3, 2, 1]
K = 5

max_sum = max_sum_window_len(num_list, K)
print(max_sum)

###################################################################################
# тест для закрепления. Испраить ошибку:
# def test_window():
#     arr = [1, 2, 3]
#     left, right = 1, 2
#     print(right - left)  # Выводит 1, а должно?

def test_window():
    arr = [1, 2, 3]
    left, right = 1, 23
    print(right - left+1)  # Выводит 1, а должно?
