leap_year = int(input("What year is it: "))

def leap():
    if leap_year % 4 == 0 and leap_year % 4 == 0 and leap_year % 100 != 0:
        print("Its A Leap Year!")
    else:
        print("Its Not A Leap Year!")

leap()