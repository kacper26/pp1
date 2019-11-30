text = '''Nam strzelać nie kazano. Wstąpiłem na działo. 
I spojrzałem na pole, dwieście armat grzmiało. 
Artyleryji ruskiej ciągną się szeregi, 
Prosto, długo, daleko, jako morza brzegi.'''

samogloski = 'aąeęiouy'
czestosci = {}

for c in samogloski:
    czestosci.setdefault(c, text.count(c))

for c, czestosc in czestosci.items():
    print(f'{c} -> {czestosc}')