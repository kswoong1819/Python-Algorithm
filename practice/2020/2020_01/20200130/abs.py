def my_abs(n):
    if type(n) == complex:
        return (n.real**2 + n.imag**2)**(1/2)
    else:
        if n<0:
            return -n
        else:
            return n
            
print(my_abs(3+4j), my_abs(0.0), my_abs(-5))