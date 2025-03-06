n = 5 #The number of data
m = 5 #partial sum want to find
data = [1, 2, 3, 2, 5]

count = 0 #The number of partial sum satisfying condition
interval_sum = 0 
end = 0 #Pointer point to ending index


for start in range(n):
    while end <= n - 1 and interval_sum < m:
        interval_sum += data[end]
        end += 1
        
    if interval_sum == m:
        count += 1
    
    interval_sum -= data[start]
        
         
         

a = [12, 45, 23, 67, 34, 89, 10, 54, 76, 32]
b = [5, 99, 38, 27, 83, 41, 62, 14, 50, 73]
n = len(a)
m = len(b)

a.sort() #To meet collect answer array a, b should be sorted
b.sort()

result = [0] * (n + m)
i = 0
j = 0
k = 0

while i < n or j < m:
    
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
        
    else:
        result[k] = b[j]
        j += 1
        
    k += 1
        
print(result)
        
     