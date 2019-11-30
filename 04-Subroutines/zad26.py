def podatek(dochod):
    if dochod <= 5000:
        return 0.17 * dochod
    nadwyzka = dochod - 5000
    return 0.17 * 5000 + 0.32 * nadwyzka


dochod = float(input('Podaj dochod: '))
print(f'Podatek nalezny: {podatek(dochod)} zl')