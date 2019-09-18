num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

def sum():
    if num1 == num2:
        first = num3 + num2
        print(first)
        return first
    if num1 == num3:
        second = num1 + num2
        print(second)
        return second
    if num3 == num2:
        third = num1 + num2
        print(third)
        return third
    elif num1 != num2 != num3:
        final = num1 + num2 + num3
        print(final)
        return final

sum()
