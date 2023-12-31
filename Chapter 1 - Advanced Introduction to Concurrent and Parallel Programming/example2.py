from timeit import default_timer as timer


def f(x):
    return x * x - x + 1


start = timer()
result = 3
for i in range(20):
    result = f(result)

print('Result is very large. Only printing the last digits:', result % 100000)
print('Sequential took: %.2f seconds' % (timer() - start))

