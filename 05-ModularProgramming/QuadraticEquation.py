import math

def podajWspolczynniki():
    a = float(input('Podaj a: '))
    b = float(input('Podaj b: '))
    c = float(input('Podaj c: '))
    return a, b, c
def obliczDelte(wspolczynniki):
    a, b, c = wspolczynniki
    return b**2-4*a*c

def obliczPierwiastki():
    a, b, c = podajWspolczynniki()
    delta = obliczDelte((a, b, c))
    if delta > 0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print('solutions:', x1, x2)
    if delta == 0:
        print(-b/(2*a))



