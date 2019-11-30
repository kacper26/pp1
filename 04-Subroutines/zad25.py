def jestImie(imie, imiona):
    return imie in imiona


wykaz_imion = ['Janek', 'Ania', 'Wojtek', 'Zosia']
imiona_do_sprawdzenia = ['Wojtek', 'Kacper']

for imie in imiona_do_sprawdzenia:
    print(f'Imie {imie} {"jest" if jestImie(imie, wykaz_imion) else "nie jest"} zawarte w wykazie imion')