numbers = []
with open('numbers.txt', 'r') as file:
    for number in file:
        numbers.append(int(number))

with open('evennumbers.txt', 'w') as even:
    for number in numbers:
        if number % 2 == 0:
            even.write(f'{number}\n') 