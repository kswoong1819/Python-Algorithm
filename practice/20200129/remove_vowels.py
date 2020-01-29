my_str = 'Life is too short, you need python'
vowels = 'aeiou'

# my_list = list(my_str)

# for i in vowels:
#     num = my_str.count(i)
#     while num > 0:
#         my_list.remove(i)
#         num -= 1
# print(''.join(my_list))

result = ''
for i in my_str:
    if i not in vowels:
        result += i
print(result)