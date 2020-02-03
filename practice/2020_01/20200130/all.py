def my_all(n):
    for i in n:
        if not i:
            return False
    else:
        return True

print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))