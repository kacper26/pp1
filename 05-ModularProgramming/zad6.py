import csv 
with open('employees.csv', newline='') as f:
    reader = csv.reader(f)
    columns = [column.upper() for column in next(reader)]
    print(f'{"#":<5} {columns[1]:<14} {columns[0]:<9} {columns[2]:<3} {columns[3]}')
    print('=' * 60)
    for index, row in enumerate(reader,1):
        name = row[0]
        surname = row[1].upper()
        age = row[2]
        email = row[3]
        print(f'{index:<5} {surname:<14} {name:<9} {age:<3} {email}')
        

    

    