import sys
sys.stdin = open('input.txt', 'r')

def two_string(m, n, m_list, n_list):
    result = 0
    for i in range(m - n + 1):
        ans = 0
        for j in range(n):
            ans += m_list[i + j] * n_list[j]
        if result < ans:
            result = ans
    return result

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    if M > N:
        print('#{} {}'.format(t+1,two_string(M, N, M_list, N_list)))
    else:
        print('#{} {}'.format(t+1,two_string(N, M, N_list, M_list)))