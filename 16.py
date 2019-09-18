#Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

#number = int(input("Enter Number: "))

#value = 17
#answer1 = number - value
#answer2 = 2 * (number - value)

#if number <= value:
    #print(answer1)
#else:
    #print(answer2)

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n-17) * 2

print(difference(22))
print(difference(14))