from typing import List, Dict
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

for key in my_dict:
    value = my_dict[key]
    print(key, value)
print()

for key, value in my_dict.items():
    print(key, value)


def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    my_list = []
    for name in age_dict:
        my_list.append(name)
    return my_list


def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    my_list = []
    for value in age_dict.values():
        my_list.append(value)
    return my_list


print(get_dict_keys(my_dict))
print(get_dict_values(my_dict))
