from random import randint

def rzucKostka():
    return randint(1, 6)

suma_rzutow = 0

print('Wyrzucone oczka: ', end='')

for _ in range(3):
    rzut = rzucKostka()
    print(f'{rzut}', end=' ')
    suma_rzutow += rzut

print(f'\nSuma rzutow: {suma_rzutow}')