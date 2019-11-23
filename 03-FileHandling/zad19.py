with open('universities.txt', 'r') as file:
    content = file.readlines()

content.sort()
    
with open('universities.txt', 'w') as file:
    file.writelines(content)