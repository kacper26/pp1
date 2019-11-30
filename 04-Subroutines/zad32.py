def transpozycja(macierz):
    kolumny = zip(*macierz)
    return [list(kolumna) for kolumna in kolumny]

macierz = [
    [1, 2, 0],
    [0, 0, 3],
    [5, 1, 1]
]

for wiersz in transpozycja(macierz):
    print(wiersz)