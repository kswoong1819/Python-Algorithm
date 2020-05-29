T = int(input())
result = []
for t in range(T):
    N = int(input())
    if N % 2:
        result.append([t+1, 'Odd'])
    else:
        result.append([t+1, 'Even'])

for tc, value in result:
    print('#{} {}'.format(tc, value))