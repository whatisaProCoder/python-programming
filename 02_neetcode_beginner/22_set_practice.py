from typing import List


def contains_duplicates(words: List[str]) -> bool:
    words_set = set(words)
    if len(words_set) < len(words):
        return True
    return False


print(contains_duplicates(['hello', 'world', 'hello']))
