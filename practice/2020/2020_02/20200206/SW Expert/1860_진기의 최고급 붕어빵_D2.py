import sys
sys.stdin = open('input.txt', 'r')

def selectSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i],a[min] = a[min], a[i]
    return a

T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))

    selectSort(customer)
    if customer[0] < M:
        print('#{} Impossible'.format(t+1))
    else:
        for i in range(1, N//K):
            m = M * i
            k = K * i
            if customer[k-1] < m:
                print('#{} Impossible'.format(t + 1))
                break
        else:
            print('#{} Possible'.format(t + 1))
