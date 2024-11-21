# WAP to print individual characters in reverse order.

def reverse(str, len):
    rev = []
    for i in range(len):
        rev.append(str[len-i-1])
    return ''.join(rev)


if __name__ == "__main__":
    print("Enter a string...")
    str = input()
    len = len(str)
    str = reverse(str, len)
    print("Reversed string...")
    print(f"{str}")
