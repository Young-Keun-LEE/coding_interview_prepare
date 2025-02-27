# n = int(input()) #LIS problem, Longest Increasing Subsequence
# soldiers = list(map(int, input().split()))
# soldiers.reverse()
# dp = [1] * n


# for i in range(1, n): # O(n ^ 2) simple algorithm
#     for j in range(i):
#         if soldiers[j] < soldiers[i]:
#             dp[i] = max(dp[i], dp[j] + 1)

        
# print(n - max(dp))        
from bisect import bisect_left

n = int(input()) #LIS problem, Longest Increasing Subsequence
soldiers = list(map(int, input().split()))
soldiers.reverse()
lis = []

for soldier in soldiers: # O(n log n) using binary_search idea
    index = bisect_left(lis, soldier)
    if index == len(lis):
        lis.append(soldier)
    else:
        lis[index] = soldier

print(n - len(lis))    