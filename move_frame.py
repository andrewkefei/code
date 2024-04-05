list1 = [100, 2, 3, 4, 5, 6, 1]
K = 3
frame = len(list1) - K
tmp = []
tmp1 = []
sum1 = sum(list1)
kk = 0

for i in range(0, frame):
    tmp = list1[i:i + frame]
    if sum(tmp) < sum1:
        tmp1 = tmp
        sum1 = sum(tmp)
        kk = i

print(tmp1)
print(sum(list1) - sum1)
print(list1[0:kk])
print(list1[kk + frame:])
