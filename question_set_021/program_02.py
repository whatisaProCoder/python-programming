# WAP to sort a string array in ascending order.

def sort_str(str, size):
    str = list(str)
    for i in range(size):
        for j in range(size-i-1):
            if str[j] > str[j+1]:
                temp = str[j]
                str[j] = str[j+1]
                str[j+1] = temp
    return ''.join(str)


if __name__ == "__main__":
    print("Enter a string...")
    str = input()
    size = len(str)
    str = sort_str(str, size)
    print("Sorted string...")
    print(str)
