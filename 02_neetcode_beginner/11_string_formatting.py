name = "Alice"
age = 25

message = "Hello, {}. You are {} years old.".format(name, age)
print(message)

message = "Hello, {1}. You are {0} years old.".format(age, name)
print(message)

message = f"Hello, {name}. You are {age} years old."
print(message)
