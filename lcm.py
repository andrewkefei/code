a = 12
b = 9

small = min(a, b)
big = max(a, b)
k = 1

while True:
    if (k * big) % small == 0:
        print(k * big)
        break
    k += 1
