N = int(input())

for i in range(N):
    print(' '*i, end='')
    print('*'*(2*(N-i)-1))
for j in range(N-2, -1 , -1):
    print(' '*j, end='')
    print('*'*(2*(N-j)-1))