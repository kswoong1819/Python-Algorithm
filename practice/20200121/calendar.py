T = int(input())
list_30 = ['04','06','09','11']
list_31 = ['01','03','05','07','08','10','12']

for t in range(T):
    check_num = input()
    year = check_num[:4]
    month = check_num[4:6]
    day = check_num[6:]
    if month == '02':
        if int(day) > 28:
            print('#{} -1'.format(t+1))
        else:
            print('#{} {}/{}/{}'.format(t+1,year,month,day))
    elif month in list_30:
        if int(day) > 30:
            print('#{} -1'.format(t+1))
        else:
            print('#{} {}/{}/{}'.format(t+1,year,month,day))
    elif month in list_31:
        if int(day) > 31:
            print('#{} -1'.format(t+1))
        else:
            print('#{} {}/{}/{}'.format(t+1,year,month,day))
    else:
        print('#{} -1'.format(t+1))