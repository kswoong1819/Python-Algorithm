N = int(input())

for i in range(1, N+1):
    print(' '*2*(N-i), end='')
    for j in range(1, i+1):
        print(j, end=' ')
    print()