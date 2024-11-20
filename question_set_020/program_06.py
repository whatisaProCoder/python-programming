""" 
Print all unique elements in an array.
If array arr = {2, 3, 2, 1, 4, 6, 4, 6}
Then output will be 3, 1
"""


def unique_elements(a, sz):
    for i in range(sz):
        j = 0
        while j < sz:
            if i != j and a[i] == a[j]:
                break
            j += 1
        if j == sz:
            print(f"{a[i]} ", end="")


if __name__ == "__main__":
    a = [2, 3, 2, 1, 4, 6, 4, 6]
    sz = len(a)
    print("Unique elements in the array...")
    unique_elements(a, sz)
