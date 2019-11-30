def miesiac(n):
    if not 1 <= n <= 12:
        return 'Podano nieprawidlowy argument'
    
    miesiace = ['Styczen', 'Luty', 'Marzec', 'Kwiecien', 'Maj', 'Czerwiec',
                'Lipiec', 'Sierpien', 'Wrzesien', 'Pazdziernik', 'Listopad', 'Grudzien']

    return miesiace[n - 1]


print(miesiac(7))
print(miesiac(9))