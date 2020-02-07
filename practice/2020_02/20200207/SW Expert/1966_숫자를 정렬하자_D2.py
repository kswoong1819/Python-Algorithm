import sys
sys.stdin = open('input.txt', 'r')

def selectSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

T = int(input())

for t in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    selectSort(num_list)

    print('#{}'.format(t+1), end=' ')
    for i in range(len(num_list)):
        print(num_list[i], end=' ')
    print()