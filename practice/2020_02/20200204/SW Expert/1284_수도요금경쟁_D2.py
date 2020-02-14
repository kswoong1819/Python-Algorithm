T = int(input())

for t in range(T):
    P, Q, R, S, W = map(int, input().split())
    A_fee = W * P
    B_fee = Q
    if W > R:
        B_fee = Q + (W-R) * S

    if A_fee < B_fee:
        print('#{} {}'.format(t+1, A_fee))
    else:
        print('#{} {}'.format(t + 1, B_fee))