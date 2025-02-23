

def solution(N, stages):
    # Initialize an array to count the number of players at each stage
    q = []
    length = len(stages) # For reduce time complexity
    for i in range(1, N + 1): # Calculate the failure rate for each stage
        if length != 0:
            failure_rate = stages.count(i) / length
        else:
            failure_rate = 0
        q.append((i, failure_rate))
        length -= stages.count(i)
    
    # Sort the stages by their failure rate in descending order
    q.sort(key = lambda x : -x[1])
    result = []
    for i in range(N):
        result.append(q[i][0])
    return result
        
print(solution(4, [4,4,4,4,4]))