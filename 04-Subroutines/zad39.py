def check(n, x, y):
    return x <= n <= y

test_cases = (
    (4, 2, 9),
    (1, 2, 3),
    (-5, -20, 20),
    (1.24, 1.235, 1.75)
)

for n, x, y in test_cases:
    if check(n, x, y):
        print(f'Liczba {n} znajduje sie w przedziale <{x}, {y}>')
    else:
        print(f'Liczba {n} nie znajduje sie w przedziale <{x}, {y}>')