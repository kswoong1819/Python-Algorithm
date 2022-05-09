import sys

sys.stdin = open('input.txt')


def fibo(n):
    fi_0 = [1, 0]
    fi_1 = [0, 1]
    for i in range(2, n + 1):
        fi_0.append(fi_0[i - 1] + fi_0[i - 2])
        fi_1.append(fi_1[i - 1] + fi_1[i - 2])
    return fi_0[n], fi_1[n]


T = int(input())

for t in range(T):
    N = int(input())
    cnt_0 = 0
    cnt_1 = 0
    tmp = fibo(N)
    print(tmp[0], tmp[1])
