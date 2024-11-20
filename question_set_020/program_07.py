# Print elements of array using recursion.

def print_array(arr, i, size):
    if i == size:
        return
    else:
        print(f"{arr[i]} ", end="")
        print_array(arr, i+1, size)


if __name__ == "__main__":
    arr = [2, 3, 4, 6, 7, 8]
    size = len(arr)
    print_array(arr, 0, size)
