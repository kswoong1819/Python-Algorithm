T = int(input())
result = []
for t in range(T):
    A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    result.append([t+1, C//A])

for tc, value in result:
    print('#{} {}'.format(tc, value))