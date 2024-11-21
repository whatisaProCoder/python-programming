# Create a multiplication table.

def print_multiplication_table(number):
    for i in range(1, 10+1):
        product = number*i
        print(f"{number} x {i} = {product}")


if __name__ == "__main__":
    number = int(input("Enter a number : "))
    print_multiplication_table(number)
