calendar = { 
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
} 
weeks = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

for month, day in calendar.items():
    print('{:10}'.format(month), '월')
    for i in weeks:
        print(i, end=' ')
    print()
    for j in range(1, day+1):
        print('{:2}'.format(j), end=' ')
        if j % 7 == 0:
            print()
    print()