osoba = {
"imie": "Marek",
"nazwisko": "Banach",
"wiek": 25,
"hobby": ["programowanie","wycieczki"],
"student": True,
"telefon":{"stacjonarny":"2233","komorkowy":"7788"}
}
#a
print(osoba)
#b
print(osoba['nazwisko'])
#c
print(osoba['hobby'])
#d
osoba['nazwisko'] = 'Nowak'
print(osoba['nazwisko'])
#e
osoba['student'] = False
print(osoba['student'])
#f
osoba['plec'] = 'Mezczyzna'
print(osoba['plec'])
#g
osoba['hobby'].append('rower')
print(osoba['hobby'])
#h
osoba['telefon']['telefon sluzbowy'] = 3131
print(osoba['telefon'])