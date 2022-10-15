import math

#Time: O(N^2)  --> TLE
def bruteForce(arr, s):
    best_so_far = math.inf
    for i in range(len(arr)):
        result = []
        sum_ = 0
        for j in range(i, len(arr)):
            if arr[j] >= S:
                return 1
            sum_ += arr[j]
            result.append(arr[j])
            if sum_ >= S:
                best_so_far = min(best_so_far, len(result))
                break

    return best_so_far    


def windowAproach(arr, target):
    window_Start = 0
    sum_ = 0
    min_length = float("inf")
    for i in range(len(arr)): 
        sum_ += arr[i]  

        while sum_ >= target: 
            min_length = min(min_length, i-window_Start+1) 
            sum_ -= arr[window_Start] 
            window_Start += 1
    if min_length == math.inf:
        return 0
    return min_length
        


arr = [2, 9, 9, 9, 0, 5, 2, 8]
S=27 
print(windowAproach(arr, S))