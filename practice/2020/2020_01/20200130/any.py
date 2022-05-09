def my_any(n):
    for i in n:
        if i:
            return True
    else:
        return False

print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))