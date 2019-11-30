import random

def getRandomInt(a=1, b=50):
    return random.randint(a, b)

odd = 0
even = 0
n = 1000

for _ in range(n):
    if getRandomInt() % 2 == 0:
        even += 1
    else:
        odd += 1

print(f'Ilosc losowan: {n}')
print(f'Liczby parzyste: {(even / n) * 100:.2f}%')
print(f'Liczby nieparzyste: {(odd / n) * 100:.2f}%')