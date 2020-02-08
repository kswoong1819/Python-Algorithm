import sys
sys.stdin = open('../list_2/input.txt', 'r')

def selectSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

def check(n):
    if n[0] == n[1] == n[2]:
        return 'triplet'
    if int(n[1]) == int(n[0]) + 1 and int(n[2]) == int(n[0]) + 2:
        return 'run'
    else:
        return 'non_gin'

def result(n1, n2):
    if (n1 == 'triplet' or n1 == 'run') and (n2 == 'triplet' or n2 == 'run'):
        return 'baby-gin'
    else:
        return 'non_gin'


for t in range(3):
    num = list(input())

    sort_num = selectSort(num)

    num1 = sort_num[:3]
    num2 = sort_num[3:]

    print(result(check(num1), check(num2)))