import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())
    words = [[] for _ in range(51)]
    for i in range(N):
        word = input()
        words[len(word)].append(word)

    print('#{}'.format(t + 1))
    for i in range(51):
        if len(words[i]) == 0:
            continue
        else:
            pr_word = sorted(set(words[i]))
            for j in pr_word:
                print(j)
