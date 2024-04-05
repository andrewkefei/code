import math

N = 9


def comb(n, k):
    a = math.factorial(n)
    b = math.factorial(k)
    c = math.factorial(n - k)
    return a // (b * c)


sum1 = 0
times1 = N
times2 = 0

while 2 * times2 <= N:
    sum1 += comb(times1, times2)
    times1 -= 1
    times2 += 1

print(sum1)
