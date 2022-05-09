N = int(input())
val = 1
while N > val:
    N -= val
    val += 1

print(N, val)

if val % 2:
    print('{}/{}'.format(val-(N-1), N))
else:
    print('{}/{}'.format(N, val-(N-1)))