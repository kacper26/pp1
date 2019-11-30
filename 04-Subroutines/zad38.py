def checkUpper(string):
    output = ''
    for c in string:
        if c.isupper():
            output += c
    return output

test_cases = (
    'string_testowy',
    'STRING_testowy',
    '123testTESTtest123',
    'a A b B c C'
)

for string in test_cases:
    print(f'{string} -> {checkUpper(string)}')