import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    bracket = input()

    ans = 0
    check = 0
    for i in range(len(bracket)):
        if bracket[i] == '(':
            check += 1
        if bracket[i] == ')' and bracket[i-1] == '(':
            check -= 1
            ans += check
        if bracket[i] == ')' and bracket[i-1] == ')':
            check -= 1
            ans += 1

    print('#{} {}'.format(t+1, ans))