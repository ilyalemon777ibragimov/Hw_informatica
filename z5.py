import math

def funcion(a):
    if a < 0 :
        return  math.sin(a**2)+2*a
    elif a >= 0 :
        return math.sqrt(a)+math.sqrt(a**2 + 1)
    else :
        return math.cos(a)

x = int(input("x >>> "))
print(funcion(x))
    