"""""
speed = int(input("Speed: "))

#point = 0

def spd():
    if speed < 70:
        print("OK")
    else:
        if speed > 70:
            
            for i in range(70, 100, 5):
                print(point)
                point += 1

spd()
"""""

def speed_check(speed):
    if speed <= 70:
        return "OK"

    else:
        speed1 = (speed-70)/5

        if speed1 <= 12:
            return print("Point:", int(speed1))

        else:
            return print("License suspended")


enter = speed_check(int(input("Enter speed: ")))
print(enter)