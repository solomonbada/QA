#https://programmingwithmosh.com/python/python-exercises-and-questions-for-beginners/

number = int(input("Enter Number: "))

def fizz_buzz():
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

fizz_buzz()