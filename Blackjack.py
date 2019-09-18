first = int(input("First Number: "))
second = int(input("Second Number: "))

def blackjack():
    if first > 0 and second > 0 and first <= 21 and second <= 21:
        if 21 - first < 21 - second:
            print(first)
        elif 21 - second < 21 - first:
            print(second)
    elif first > 0 and second > 0 and first > 21 and second <= 21 :
        print(second)
    elif first > 0 and second > 0 and first <= 21 and second > 21:
        print(first)
    elif first > 21 and second > 21:
        print(0)

blackjack()
