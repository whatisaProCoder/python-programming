number_string = '1, 2, 3'

string_list = number_string.split(', ')

print(string_list)

number_list = []
for element in string_list:
    integer = int(element)
    number_list.append(integer)

print(number_list)
