def mediana(tab):
    sorted_tab = sorted(tab)
    n = len(sorted_tab)
    if n % 2 == 0:
        return (sorted_tab[n // 2] + sorted_tab[n // 2 - 1]) / 2
    else:
        return sorted_tab[n // 2]


# dominanta to element wystepujacy w tablicy najczesciej
# jesli takich elementow jest kilka, to wszystkie sa dominantami (dlatego funkcja zwraca tablice)
def dominanta(tab):
    num_count = {}
 
    for n in tab:
        if n not in num_count:
            num_count[n] = tab.count(n)

    highest_counter = max(num_count.values())
    return [n for n in num_count if num_count[n] == highest_counter]


tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]

print(f'Mediana: {mediana(tab)}')
print(f'Dominanta: {dominanta(tab)}')