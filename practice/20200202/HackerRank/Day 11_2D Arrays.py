if __name__ == '__main__':
    arr = []
    result_list = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(4):
        for j in range(4):
            result = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            result_list.append(result)

    answer = result_list[0]
    for i in result_list:
        if answer < i:
            answer = i
    print(answer)