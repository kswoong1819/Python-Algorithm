import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
road = list(map(int, input().split()))

num_list = []
ans = 0
for i in range(1,N):
    if road[i-1] < road[i]:
        num_list.append(road[i-1])
        num_list.append(road[i])
        if len(num_list) != 0 and i == N-1:
            result = max(num_list) - min(num_list)
            if result > ans:
                ans = result
    if road[i-1] >= road[i]:
        if len(num_list) != 0:
            result = max(num_list) - min(num_list)
            if result > ans:
                ans = result
            num_list = []

print(ans)