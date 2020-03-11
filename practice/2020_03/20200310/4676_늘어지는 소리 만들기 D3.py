import sys
sys.stdin = open('input.txt')

T = int(input())
res = []
for t in range(T):
    string = input()
    H = int(input())
    position = list(map(int, input().split()))

    check = [0] * 21
    for i in position:
        check[i] += 1

    result = ''
    for i in range(len(string)):
        result += '-'*check[i]+string[i]
    result += '-'*check[len(string)]

    res.append('#{} {}'.format(t+1, result))
print('\n'.join(res))