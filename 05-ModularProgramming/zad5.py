import statistics

dane = [21600, 4350, 3920, 5590, 3250, 4010]
a = statistics.mean(dane)
print(a)

m = statistics.median(dane)
print(m)

print(f'Odchylenie standardowe danych wynosi {(statistics.stdev(dane))}')
                              