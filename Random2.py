user_input = int(input("What is your number: "))
user_input2 = input("Triple or Double: ")

def user():
    if user_input2 == "double":
        double = user_input * 2
        return double
    elif user_input2 == "triple":
        triple = user_input * 3
        return triple

print(user())
