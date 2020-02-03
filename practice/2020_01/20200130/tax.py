def tax(won):
    if won <= 1200:
        return won * 0.06
    elif 1200 < won <= 4600:
        return 1200*0.06 + (won-1200)*0.15
    else:
        return 1200*0.06 + (4600-1200)*0.15 + (won-4600)*0.35

print(tax(1200))
print(tax(4600))
print(tax(5000))