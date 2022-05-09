import sys
sys.stdin = open('input.txt', 'r')

def selectSort(n):
    for i in range(len(n)-1):
        min = i
        for j in range(i, len(n)):
            if n[min] > n[j]:
                min = j
        n[i] ,n[min] = n[min], n[i]
    return n

T = int(input())

for t in range(T):
    num_count = input()
    N = list(map(int, input() .split()))
    selectSort(N)
    sort_list = []
    for i in range(5):
        sort_list.append(str(N[-i-1]))
        sort_list.append(str(N[i]))
    print('#{}'.format(t+1),' '.join(sort_list))