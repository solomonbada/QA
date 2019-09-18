#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
user_first = input("What is your first name: ")[::-1]
user_last = input("What is your last name: ")[::-1]

print(user_first,"", user_last)

#".join(reversed(shout))"