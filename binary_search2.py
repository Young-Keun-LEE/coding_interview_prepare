def find_max_height(Trees, M): # Find max height of tree cutter
    start = 0 # Minimum height of cutter
    end = max(Trees) # Maximum of cutter
    max_height = 0

    while start <= end:
        mid = (start + end) // 2
        if cut_tree(Trees, mid) >= M: # This case satisify condition
            max_height = mid
            start = mid + 1


        elif cut_tree(Trees, mid) < M: # This case doesn't
            end = mid - 1
    
    return max_height

def cut_tree(Trees, h): # How many trees do you have if you cut trees with h heigth
    cut_len = 0
    for t in Trees:
        remainder = t - h
        if remainder > 0:
            cut_len += remainder
    return cut_len

N, M = map(int, input().split(" "))
Trees = list(map(int, input().split(" ")))
print(find_max_height(Trees, M))