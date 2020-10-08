from string import ascii_lowercase

L = list(ascii_lowercase)
print(L)


def solution(S):
    L = len(S)
    L2 = len(S[0])
    for i in range(L - 1):
        for j in range(i + 1, L):
            for k in range(L2):
                if S[i][k] == S[j][k]:
                    return [i, j, k]
    return []


# S = ["abcdefghigk", "abc"]
S = []
for i in range(21):
    a = L[i: i+6]
    S.append(''.join(a))
L2 = list(reversed(L))
for i in range(21):
    a = L2[i: i+6]
    S.append(''.join(a))
print(S)
print(solution(S))



