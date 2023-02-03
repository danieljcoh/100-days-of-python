# WRITE A PROGRAM THAT DETERMINES IF ANY INPUT YEAR IS A LEAP YEAR OR NOT


year = int(input("Which year do you want to check? "))


###on every year that is evenly divisible by 4 
###**except** every year that is evenly divisible by 100 
###**unless** the year is also evenly divisible by 400


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")