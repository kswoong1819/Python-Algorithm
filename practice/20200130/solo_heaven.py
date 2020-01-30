def lonely(num_list):
    result_list = [num_list[0]]
    for i in num_list:
        if result_list[-1] != i:
            result_list.append(i)
    return result_list
        
print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4,4,4,3,3]))