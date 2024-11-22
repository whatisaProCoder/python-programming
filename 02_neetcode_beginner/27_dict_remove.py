from typing import List, Dict


def one():
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    my_dict.pop('a')

    print(my_dict)

    rem = 'c'
    if rem not in my_dict:
        print(f"{rem} not in the dictionary. So can't remove.")
    else:
        my_dict.pop(rem)

    print(f"After removing {rem}...")
    print(my_dict)


def remove_keys(my_dict: Dict[str, int], keys_remove: List[str]) -> Dict[str, int]:
    for keys_to_remove in keys_remove:
        if keys_to_remove in my_dict:
            my_dict.pop(keys_to_remove)
    return my_dict


print(remove_keys({'a': 1, 'b': 2, 'c': 3}, ['a', 'c']))
