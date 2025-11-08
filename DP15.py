n, k = map(int, input().split(" ")) # n = number of coin types, k = target amount
coins = []
dp = [0] * (k + 1) # Initialize dp table
dp[0] = 1 # Base case: one way to make 0 (use no coins)

for _ in range(n): # Read available coin in list
    coins.append(int(input()))

for coin in coins: # Fill the dp table
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]
        
print(dp[k])
