arr = [7,4,2,0,0,6,0,7,0]
list = []

for a in arr:
    result = 9
    for b in arr:
        if a <= b:
            result -= 1
    list.append(result)

max_num = list[0]
for i in range(1,len(list)):
    if max_num < list[i]:
        max_num = list[i]

print(max_num)


# def = build_data(data):
#     for i in range(0,100)
#         data[i]
#
# if __name__ == '__main__':
#     int data[100];
#     for i in range(0,100)
#         build_data(data)
#
#         print _result