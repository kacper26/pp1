numbers = []
with open('numbers.txt', 'r') as file:
    for number in file:
        numbers.append(int(number))
numbers.sort()
print(' '.join(str(n) for n in numbers))
    