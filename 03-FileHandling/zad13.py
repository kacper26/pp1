tab = [32, 16, 5, 8, 24, 7]
tab.sort()
print(tab)
with open('tab.txt', 'w') as file:
    for line in tab:
        file.write(f'{line}\n')