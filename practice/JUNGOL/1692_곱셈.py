A = int(input())
B = b = int(input())

for i in range(3):
    print(A * (B % 10))
    B = B//10

print(A*b)