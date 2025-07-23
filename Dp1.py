import sys
input = sys.stdin.readline

result = []
dp = [False] * 21 ** 3 # index = a * 21 + b * 21 + c
def idx(a, b, c):
    return a * 21 ** 2 + b * 21 + c

def w(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if dp[idx(a, b, c)] is not False:
        return dp[idx(a, b, c)]
    
    if a < b and b < c:
        if dp[idx(a, b, c)] is False:
            dp[idx(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
            return dp[idx(a, b, c)]

    else:
        if dp[idx(a, b, c)] is False:
            dp[idx(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
            return dp[idx(a, b, c)]

    



while True:
    a, b, c  = map(int, input().strip().split(" "))
    
    if a == -1 and b == -1 and c == -1:
        break
    
    else:
        result.append(f"w({a}, {b}, {c}) = {w(a,b,c)}")

sys.stdout.write("\n".join(result))