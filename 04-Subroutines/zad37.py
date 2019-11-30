def selectDistinct(numbers):
    output = []
    for n in numbers:
        if numbers.count(n) == 1:
            output.append(n)
    return output

test_cases = (
    [1, 2, 3, 4],
    [1, 1, 2, 2],
    [1, 1, 1, 1],
    [1, 1, 2, 2, 3]
)

for numbers in test_cases:
    print(f'{numbers} -> {selectDistinct(numbers)}')