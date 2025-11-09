# Input number of rows (M) and columns (N)
M, N = map(int, input().split(" "))

# Initialize original grid and list for sorting cells by height
heights = []
buildings = [[0] * N for _ in range(M)]

# Read grid and populate heights list with (row, col, height)
for row in range(M):
    string = list(map(int, input().split(" ")))
    for col in range(N):
        heights.append((row, col, string[col]))
        buildings[row][col] = string[col]

# Sort cells by height in ascending order (for bottom-up DP)
heights.sort(key=lambda x: x[2])

# Initialize DP table; dp[x][y] = number of paths from (x, y) to bottom-right
dp = [[0] * N for _ in range(M)]
dp[M - 1][N - 1] = 1  # Base case: only 1 path from destination to itself

# Bottom-up DP: process cells from lowest height to highest
for x, y, _ in heights:
    # Explore all four directions: up, down, left, right
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        # Check bounds and ensure the next cell is higher (reverse of downhill)
        if 0 <= nx < M and 0 <= ny < N and buildings[x][y] < buildings[nx][ny]:
            dp[nx][ny] += dp[x][y]  # Accumulate paths from current cell

# Print number of paths from top-left to bottom-right
print(dp[0][0])
