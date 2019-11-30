# n - numer elementu
def fibonacci(n, a=0, b=1):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return a + fibonacci(n - 1, b, a + b)

# fib1 = 0
# fib2 = 1
# fib3 = 1
# fib4 = 2
# fib5 = 3
# fib6 = 5
# fib7 = 8
# ...

for n in range(1, 21):
    print(fibonacci(n), end=' ')
