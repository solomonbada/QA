#Write a Python program to count the number 4 in a given list.

def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count += 1

    return count

print(list_count_4([1,2,6,7,4,4]))


list = [1, 3, 4, 2, 3, 3]

zero = 0
for numb in list:
    if numb == 3:
        zero += 1

print(zero)
