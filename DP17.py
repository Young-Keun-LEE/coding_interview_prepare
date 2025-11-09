import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    # Base case: if we reached the bottom-right corner, there's 1 path
    if x == (M - 1) and y == (N - 1):
        return 1

    # If already computed, return the stored result to avoid recomputation
    if dp[x][y] != -1:
        return dp[x][y]    
    
    dp[x][y] = 0
    # Explore all four directions: up, down, left, right
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        # Check bounds and ensure next cell is lower (downhill)
        if 0 <= nx < M and 0 <= ny < N and buildings[nx][ny] < buildings[x][y]:
            dp[x][y] += dfs(nx, ny)  # Add paths from the next cell
    
    return dp[x][y]  # Return total paths from current cell

# Input number of rows (M) and columns (N)
M, N = map(int, input().split(" "))

buildings = []
# Initialize memoization table with -1
dp = [[-1] * N for _ in range(M)]

# Input heights of each cell
for _ in range(M):
    buildings.append(list(map(int, input().split(" "))))
    
# Compute and print number of downhill paths from top-left to bottom-right
print(dfs(0, 0))


