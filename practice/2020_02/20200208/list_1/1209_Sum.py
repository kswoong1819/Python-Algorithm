import sys
sys.stdin = open('../list_2/input.txt', 'r')

for t in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    check_list = []
    d1_sum = 0
    d2_sum = 0
    for i in range(100):
        d1_sum += arr[i][i]
        d2_sum += arr[i][99-i]
        r_sum = 0
        c_sum = 0
        for j in range(100):
            r_sum += arr[i][j]
            c_sum += arr[j][i]
        check_list.append(r_sum)
        check_list.append(c_sum)
    check_list.append(d1_sum)
    check_list.append(d2_sum)

    print('#{}'.format(t+1))
    print(max(check_list))