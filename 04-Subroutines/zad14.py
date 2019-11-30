def wystepuje(liczba, tablica):
    if liczba in tablica:
        print('Podana liczba wystepuje w tablicy')
    else:
        print('Podana liczba nie wystepuje w tablicy')

n = 23
tab = [15, 38, 7, 23, 14]

wystepuje(n, tab)