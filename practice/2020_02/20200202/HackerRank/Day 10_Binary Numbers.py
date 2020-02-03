def binary(n):
    num = format(n, 'b')
    count = 0
    count_list = []
    for i in range(len(num)):
        if int(num[i]) == 1:
            count += 1
        else:
            count_list.append(count)
            count = 0
    else:
        count_list.append(count)
    return max(count_list)

n = int(input())
print(binary(n))