def make_square(arr):
    result = []
    mid = 0
    for i in range(len(arr)): 
        if arr[i] >= 0:
            mid = i
            break
    left = mid-1
    right = mid
    print(left, right)
    # [-2, -1, 0, 2, 3]
    while left > 0 or right < len(arr):
        if (arr[left])**2 < (arr[right])**2:
            result.append((arr[left])**2)
            left -= 1
        else:
            result.append((arr[right])**2)
            right += 1
        
    while left >= 0:
        result.append((arr[left])**2)
        left -= 1
    
    while right < len(arr):
        result.append((arr[right])**2)
        right += 1
            
    return result
arr = [-5,-3,-2,-1]
print(make_square(arr))