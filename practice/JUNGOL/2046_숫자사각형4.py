N, M = map(int, input().split())

if M == 1:
    for i in range(N):
        for j in range(N):
            print(i+1, end=' ')
        print()
if M == 2:
    for i in range(N):
        if i % 2:
            for j in range(N, 0, -1):
                print(j, end=' ')
            print()
        else:
            for j in range(1, N+1):
                print(j, end=' ')
            print()
if M == 3:
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(i*j, end=' ')
        print()