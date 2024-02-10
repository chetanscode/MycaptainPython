def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print the first 15 Fibonacci numbers
for i in range(15):
    print(fibonacci(i))
