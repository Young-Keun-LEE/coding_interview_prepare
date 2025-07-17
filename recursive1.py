# Implement merge sort

def merge_sort(A,p,r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A,p,q)
        merge_sort(A,q + 1,r)
        merge(A,p,q,r)

def merge(A, p, q, r):
    i = p
    j = q + 1
    tmp = []
    count = 0
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while i <= q:
        tmp.append(A[i])
        i += 1
    
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    for i in range(len(tmp)):
        A[p + i] = tmp[i]
        log.append(tmp[i])

log = []
N, K = map(int, input().split(" "))
A = list(map(int, input().split()))
merge_sort(A, 0, len(A) - 1)

if K <= len(log):
    print(log[K - 1])
else:
    print("-1")