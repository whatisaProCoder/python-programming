def one():
    try:
        # code that might cause an error
        result = 10 / 0
    except:
        print("An error occurred!")

    print("This will be printed regardless.")


def divide_numbers(a: str, b: str) -> None:
    try:
        a = int(a)
        b = int(b)
        division = a / b
        print(f"Division : {division}")
    except Exception as error:
        print("Error :", error)


def divide_numbers2(a: str, b: str) -> None:
    try:
        a = int(a)
        b = int(b)
        division = a / b
        print(f"Division : {division}")
    except ValueError:
        print("Value Error ")
    except ZeroDivisionError:
        print("Zero Division Error ")
    except Exception as error:
        print("Error :", error)


divide_numbers('10', '2')
divide_numbers('10', '0')
divide_numbers('10', 'not a number')
print()

divide_numbers2('10', 'not a number')
divide_numbers2('10', '0')
