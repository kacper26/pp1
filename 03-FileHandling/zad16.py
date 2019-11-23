import re 
 
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C' 
cyfry = re.findall(r'\d+', komunikat)

print(sum([int(temp) for temp in cyfry]) / len(cyfry))