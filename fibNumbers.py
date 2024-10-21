def fibonacci(n):
    '''Calculate the fibonacci number of n'''

    # Base case
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(f"F({i}) = ", fibonacci(i))

# Test the fibonacci function with a large number
#fibonacci(2**10)