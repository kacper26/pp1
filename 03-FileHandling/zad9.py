with open('NoEducation.txt','r') as file:
    for n, line in enumerate(file, 1):
        print(f'{n} ', end='')
        print(line, end='')