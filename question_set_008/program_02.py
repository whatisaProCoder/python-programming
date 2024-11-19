def fibonacci_term(num_terms):
    if num_terms == 1:
        return 0
    elif num_terms == 2:
        return 1
    else:
        return fibonacci_term(num_terms-1)+fibonacci_term(num_terms-2)


if __name__ == "__main__":
    num_terms = int(input("Enter number of terms : "))
    for i in range(1, num_terms+1):
        print(f"{fibonacci_term(i)} ", end="")
