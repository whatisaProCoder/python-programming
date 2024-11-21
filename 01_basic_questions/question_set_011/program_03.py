# Find all 3 digit Armstrong numbers.

def get_number_of_digits(number):
    number_of_digits = 0
    while number > 0:
        digit = number % 10
        number_of_digits += 1
        number = number//10
    return number_of_digits


def get_sum_of_digits_powered(number):
    summation = 0
    number_of_digits = get_number_of_digits(number)
    while number > 0:
        digit = number % 10
        summation += pow(digit, number_of_digits)
        number = number//10
    return summation


def isArmstrong(number):
    if get_sum_of_digits_powered(number) == number:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Armstrong numbers till 999...")
    for i in range(100, 999+1):
        if isArmstrong(i):
            print(f"{i} ", end="")
