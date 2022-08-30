from functools import reduce

fibonacci = lambda n: reduce(lambda a: a+[a[-1]+a[-2]], range(n-2), [0, 1])

valores = fibonacci(7)
print(valores)