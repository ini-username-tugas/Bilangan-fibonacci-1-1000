def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci = list(fib(1000))
print (fibonacci)

def removeganjil(y):
    new_numbers = []
    for x in y:
            if x % 2 == 0:
                new_numbers.append(x)
    return new_numbers

fibonaccigenap = (removeganjil(fibonacci))

print (fibonaccigenap)
print (sum(fibonaccigenap))