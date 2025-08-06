def binary_search(N, K):
    start = 1
    end = N * N
    answer = 0    

    while start <= end:
        mid = (start + end) // 2
        if count_less_num(N, mid) >= K:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer

def count_less_num(N, ref):
    count = 0
    for i in range(1, N + 1):
        count += min(N, ref // i)
    return count

N = int(input()) #Among N ^ 2 numbers, find k th smallest number
K = int(input())
print(binary_search(N, K))
