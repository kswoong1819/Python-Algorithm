def positive_sum(*numbers):
    result = 0
    for number in numbers:
        if number > 0:
            result += number
    return result

print(positive_sum(1, -4, 7, 12))
print(positive_sum(-1, -2, -3, -4))