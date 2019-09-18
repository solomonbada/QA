user_input = int(input("Array Size: "))

numbers = []
num = []
start = 0

for i in range(user_input + 1):
    numbers.append(i)
    for j in range(1):
        num.append((i*10))
    start += 1

print(numbers)
print(num)
