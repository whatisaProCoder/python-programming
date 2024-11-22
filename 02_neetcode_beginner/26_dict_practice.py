from typing import Dict


def count_characters(word: str) -> Dict[str, int]:
    count = {}
    for char in word:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count


print(count_characters("hello"))
