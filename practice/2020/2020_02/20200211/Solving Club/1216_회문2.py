def palin(ch_list):
    for i in range(len(ch_list)//2):
        if ch_list[i] != ch_list[-i-1]:
            return False
    return True

for t in range(10):
    T = int(input())
    matrix = [list(input()) for _ in range(100)]

    def max():
        result = 0
        for N in range(99,0,-1):
            for i in range(100):
                for j in range(100 - N + 1):
                    ch_list = []
                    for k in range(j, j + N):
                        ch_list.append(matrix[i][k])
                    if palin(ch_list):
                        tmp = len(ch_list)
                        if result < tmp:
                            result = tmp
                            return result

    def max_2():
        result2 = 0
        for N in range(99,0,-1):
            for i in range(100 - N + 1):
                for j in range(100):
                    ch_list = []
                    for k in range(i, i + N):
                        ch_list.append(matrix[k][j])
                    if palin(ch_list):
                        tmp = len(ch_list)
                        if result2 < tmp:
                            result2 = tmp
                            return result2

    a= max()
    b= max_2()

    if a>b:
        ans = a
    else:
        ans = b



    print('#{} {}'.format(T,ans))