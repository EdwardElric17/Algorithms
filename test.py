import sys
input = sys.stdin()
n = input
ks = list()
i = 1
while n != 0:
    if n - i < i + 1 and n - i != 0:
        i += 1
        continue
    else:
        ks.append(i)
        n -= i
        i += 1
print(len(ks))
for i in ks:
    print(i, end=' ')