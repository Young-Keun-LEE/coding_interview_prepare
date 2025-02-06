def find_length(array, N, M):
    start = 0 #Set start index
    end = max(array) #Set end index
    
    while start <= end:
        sum = 0
        mid = (start + end) // 2
        
        for length in array:
            if length - mid > 0:
                sum += (length - mid)
            
        if sum == M:
            return mid
        
        elif sum < M:
            end = mid - 1
            
        else:
            start = mid + 1
        
            

N, M = map(int, input().split()) # N : The number of rice cake, M: Required length of rice cake
array = list(map(int, input().split()))
print(find_length(array, N, M))