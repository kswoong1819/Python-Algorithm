def fee(min, km):
    min_fee = min * 120
    insurance = min//30 * 525
    if km > 100:
        km_fee = 170*100 + (km-100)*170/2
    else:
        km_fee = km*170
    
    return min_fee + insurance + km_fee

print(fee(50, 50))
print(fee(600, 110))