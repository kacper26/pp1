def suma(tablica):
    print('Tablica: ', end='')
    for n in tablica:
        print(n, end=' ')
    print(f'\nSuma wartosci: {sum(tablica)}')

suma([4, 3, 7, 1, 3])