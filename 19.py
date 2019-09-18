"""
def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is" + str

print(new_string("Array"))
print(new_string("Isnew"))
"""

user = input("Enter Word: ")


if len(user) >= 2 and user[:2] == "Is":
    print(user)
else:
    print("Is " + user)

