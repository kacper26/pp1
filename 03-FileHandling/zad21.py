count = 0
summed = 0

with open('numbersinrows.txt', 'r') as file:
    for line in file:
        nums = line.split(',')
        count += len(nums)
        summed += sum(int(n) for n in nums)

print(f'ilosc: {count}')
print(f'suma: {summed}')