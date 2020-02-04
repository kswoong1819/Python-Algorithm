import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    num_list = [x for x in range(1,13)]
    count = 0
    for i in range(1<<12):
        list_subset = []
        subset_sum = 0
        for j in range(12):
            if i & (1<<j):
                list_subset.append(num_list[j])
                subset_sum += num_list[j]
        if len(list_subset) == N and subset_sum == K:
            count += 1
    print('#{} {}'.format(t+1,count))