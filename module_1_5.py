# Teplova // I need to create a variable with different type data (tuple). Tuple marks () or without (). Output it
immutable_var  = "goggles", "bat", "basket", "hoop", "balls", "racket", 305, 1001, 89, 17, 4, True
print(immutable_var)
# Try to change the element of the tuple and explain
#immutable_var_[6]  = 700
#print(immutable_var_6)
# the program gives an error that the fifth line doesn't work. It's an immutable variable (the element of the tuple does not change)
# I can change the internal element of the tuple if it's a list
immutable_var  = ["goggles", "bat", "basket", "hoop", "balls", "racket",305, 1001, 89, 17], 4, True
immutable_var[0][3] = "hook"
print(immutable_var)
# Create a variable with the list (don't forget []), change, output it.
mutable_list = ["cost", "assets", "poverty"]
print(mutable_list)
mutable_list[1] = "debt"
print(mutable_list)
mutable_list.append("values")
print(mutable_list)
mutable_list.extend(["assess"])
print(mutable_list)
mutable_list.remove("values")
print(mutable_list)