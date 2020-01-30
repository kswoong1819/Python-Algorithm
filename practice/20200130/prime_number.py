numbers = [26, 39, 51, 53, 57, 79, 85]

for num in numbers:
    for i in range(2,num):
        if num % i == 0:
            print('{} 는 소수가 아닙니다. {} 는 {} 의 인수입니다.'.format(num,i,num))
            break
    else:
        print('{} 는 소수입니다.'.format(num))