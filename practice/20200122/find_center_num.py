N = int(input())
rannum = list(map(int, input().split(' ')))
sort_num = sorted(rannum)
print(sort_num[N//2])