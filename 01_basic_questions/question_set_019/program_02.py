# WAP to count the total number of duplicate elements in an array.

a = [1, 2, 3, 4, 5, 6, 5, 4, 2, 5]
sz = len(a)

mark = []
for i in range(sz):
    mark.append(-1)

freq_dupl = 0
for i in range(sz):
    freq = 0
    if mark[i] == 0:
        continue
    for j in range(sz):
        if a[i] == a[j]:
            freq += 1
            mark[j] = 0
    if freq > 1:
        freq_dupl += 1

print(f"Number of duplicates : {freq_dupl}")
