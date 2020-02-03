def q5(number):
    num = str(number)
    if len(num) == 1:
        return True
    else:
        for i in range(0, len(num)-1):
            if int(num[i]) - int(num[i + 1]) == 1 and int(num[i + 1]) - int(num[i]) == 1:
                return False
        else:
            return True

if __name__ == '__main__':
    print(q5(8))
    print(q5(79))
    print(q5(5567))
    print(q5(4343456))
    print(q5(89098))
    print(q5(123450))
