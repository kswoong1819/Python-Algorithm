basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
count_fruits = count_others = 0


for i in basket_items:
    if i in fruits:
        count_fruits += basket_items[i]
    else:
        count_others += basket_items[i]
print('과일은 {}개이고, {}개는 과일이 아닙니다.'.format(count_fruits, count_others))