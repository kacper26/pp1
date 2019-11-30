tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]

def recursiveSum(numbers):
    result = 0
    for n in numbers:
        if isinstance(n, int):
            result += n
        elif isinstance(n, list):
            result += recursiveSum(n)
    
    return result

print(recursiveSum(tab))