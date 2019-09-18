temp = int(input("What is the temperature: "))
season = input("What is the season: ")

def too_hot():
    if season == "isSummer":
        if temp >= 60 and temp <= 100:
            print(True)
            return True
        else:
            print(False)
            return False
    elif season != "summer":
        if temp >= 60 and temp <= 90:
            print(True)
            return True
        else:
            print(False)
            return False

too_hot()