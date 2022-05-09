import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cnt = 0
for t in range(N):
    word = input()
    check = [word[0]]
    for i in range(1, len(word)):
        if word[i-1] != word[i]:
            check.append(word[i])

    tmp = []
    for i in range(len(check)):
        if check[i] not in tmp:
            tmp.append(check[i])
    if len(tmp) == len(check):
        cnt += 1

print(cnt)