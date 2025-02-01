def fibonachi(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    
    return fibonachi(N - 2) + fibonachi(N - 1)

N = int(input())
print(fibonachi(N))


