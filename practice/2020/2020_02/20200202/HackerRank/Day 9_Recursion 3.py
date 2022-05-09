def factorial(n):
    if n == 1:
        return n
    return factorial(n-1)*n

n = int(input())
result = factorial(n)
print(result)