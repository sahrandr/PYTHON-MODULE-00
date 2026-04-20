def ft_water_reminder():
    watering = int(input("Days since last watering: "))
    if 2 < watering:
        print("Water the plants!")
    else:
        print("Plants are fine")
