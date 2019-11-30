def suma(N):
    if N == 1:
        return 1
    return N + suma(N - 1)

print(f'Suma liczb naturalnych z zakresu <1, 500> wynosi {suma(500)}')