#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

ans = num1 + num2 + num3

if num1 == num2 == num3:
    ans1 = ans*3
    print(ans1)
else:
    print(ans)


