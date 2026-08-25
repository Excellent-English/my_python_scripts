def funkcja_fibonacci(n):
    # base case
    print(n)
    if n <= 1:
        return n
    return funkcja_fibonacci(n - 1) + funkcja_fibonacci(n - 2)

print(funkcja_fibonacci(6))