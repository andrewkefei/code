N = 100
set1 = set([i for i in range(2, N + 1)])

for i in range(2, N + 1):
    for j in range(2, i):
        if i % j == 0:
            set1 = set1 - {i}
            break

print(sorted(set1))
print(len(set1))
