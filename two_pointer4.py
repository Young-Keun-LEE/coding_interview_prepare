from bisect import bisect_right

def dfs(idx, current_weight, items, result, limit):
    """
    Recursive DFS to generate all possible subset sums of 'items'
    that do not exceed the given 'limit'.
    """
    # Base case: all items processed
    if idx == len(items):
        if current_weight <= limit:
            result.append(current_weight)
        return
    
    # Case 1: include the current item
    dfs(idx + 1, current_weight + items[idx], items, result, limit)
    # Case 2: exclude the current item
    dfs(idx + 1, current_weight, items, result, limit)


# Input: N = number of items, C = maximum bag capacity
N, C = map(int, input().split())
items = list(map(int, input().split()))

# Step 1: Split items into two groups (for "Meet in the Middle" approach)
A = items[:N//2]
B = items[N//2:]

# Step 2: Generate all possible subset sums for each group
sum_A, sum_B = [], []
dfs(0, 0, A, sum_A, C)
dfs(0, 0, B, sum_B, C)

# Step 3: Sort one side for binary search
sum_B.sort()

# Step 4: For each sum in A, count compatible sums in B
# that keep total weight ≤ C using binary search
answer = 0
for a in sum_A:
    answer += bisect_right(sum_B, C - a)

# Step 5: Print total number of valid combinations
print(answer)
