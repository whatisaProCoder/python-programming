# WAP to count the frequency number of each element.

a = [1, 2, 3, 4, 5, 6, 5, 4, 2]
sz = len(a)

mark = []
for i in range(sz):
    mark.append(-1)

for i in range(sz):
    freq = 0
    if mark[i] == 0:
        continue
    for j in range(sz):
        if a[i] == a[j]:
            freq += 1
            mark[j] = 0
    if freq > 0:
        print(f"{a[i]} => {freq}")
