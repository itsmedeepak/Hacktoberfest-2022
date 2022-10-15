# # Time: O(N*K) | Space: O(1)
# def bruteForce(arr, k, avg):
#     for i in range(len(array)-k+1):
#         avg = [] 
#         sum_ = 0.0
#         for j in range(i, k+i):
#             sum_ += array[j]
#         avg.append(sum_/k)
#     return avg

# def usingWindow(arr, k, avg):
#     avg = []
#     windowStart = 0
#     windowSum = 0.0
#     for windowEnd in range(len(arr)):
#         windowSum += arr[windowEnd] # add the next element
#         # slide the window, we don't need to slide if we've not hit the required window size of 'k'
#         if windowEnd >= k - 1:
#             avg.append(windowSum/k) # calculate the average 
#             windowSum -= arr[windowStart] # subtract the element going out
#             windowStart += 1 # slide the window ahead
#     return avg

# time : N*k

# def Longest_Substring_with_K_Distinct_Characters(string, k):
#     max_len = 0
#     for i in range(len(string)):
#         store = ''
#         for j in range(i, len(string)):
#             if len(set(store)) < k:
#                 store += string[j]
#             elif string[j] in store:
#                 store += string[j]
#             else:
#                 break
#         max_len = max(max_len, len(store))
#     return max_len


String = "abbbb" 
window_start = 0
map_ = {}
max_ans = 0
for window_end in range(len(String)):
    right_char = String[window_end]
    if right_char in map_:
        window_start = max(window_start, map_[right_char]+1)
    map_[right_char] = window_end    
    max_ans = max(max_ans, window_end - window_start + 1) 
print(max_ans)