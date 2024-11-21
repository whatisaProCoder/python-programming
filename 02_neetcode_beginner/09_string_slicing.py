def get_substring(string: str, start: int, end: int) -> str:
    if end > len(string):
        return string
    return string[start:end]


def last_n_characters(string: str, n: int) -> str:
    start = len(string) - n
    return string[start:]


print(get_substring("Pritam Debnath", 1, 10))
print(last_n_characters("Pritam Debnath", 7))
