# asking user for the time and calling convert function
def main():
    meal_time = input("What time is it? ")
    meal_time = convert(meal_time)

# evaluating the result of the convert() function and printing the appropriate meal to have
    if meal_time >= 7.0 and meal_time <= 8.0 :
        print("Breakfast time")
    elif meal_time >= 12.0 and meal_time <= 13.0 :
        print("Lunch time")
    elif meal_time >= 18.0 and meal_time <= 19.0 :
        print("Dinner time")
    else:
        print("")

# evaluating if the input time is in the 12 hr format and in a.m., converting the time values and outputting the result as a float for the main() function
def convert(time):
    if "a.m." in time:
        x, y = time.replace(".","").replace("am","").split(":")
        x = float(x) * 60
        y = float(y)
        z = (x + y) / 60
        return float(z)
# evaluating if the input time is in the 12hr format and in p.m. and if it is, calculating the proper time as a float. exception given to 12:xx pm because we do not need to add 12
    elif "p.m." in time:
        x, y = time.replace(".","").replace("pm","").split(":")
        x = float(x)
        y = float(y)
        if x != 12.0:
            x = (x + 12) * 60
            z =(x + y) / 60
            return float(z)
        else:
            x = float(x) * 60
            y = float(y)
            z = (x + y) / 60
            return float(z)
# calculation for 24hr time format input
    else:
        x, y = time.split(":")
        x = float(x) * 60
        y = float(y)
        z = (x + y) / 60
        return z


if __name__ == "__main__":
    main()
