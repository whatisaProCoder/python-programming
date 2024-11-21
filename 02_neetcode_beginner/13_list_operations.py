my_list = [1, 2, 3]

if my_list:
    print("List is not empty.")
else:
    print("List is empty.")

key = 4
if key in my_list:
    print(f"{key} is present.")
else:
    print(f"{key} is not present.")

key = 2
if key not in my_list:
    print(f"{key} not in the list.")
else:
    print(f"{key} is present in the list.")
