import math
def is_prime_number(x):
    for i in range(2, x - 1): #Consider all cases
        if x % i == 0:
            return False
    
    return True

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def find_prime_number(n): #Find prime number between 1 and n + 1 using Sieve of Eratosthenes
    array = [True] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    
    for i in range(2, n + 1):
        if array[i]:
            print(i, end = " ")
    
    
    
    
find_prime_number(100000)