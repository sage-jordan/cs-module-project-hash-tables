
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Recursive funcations require:
## base case
## move toward the base case 
## function has to call itself

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(5)

(4) + (3)

(3) + (2) & (2) + (1)

(2) + (1) & (1) + (0) & (1) + (0) + (0)

(1) + (0)