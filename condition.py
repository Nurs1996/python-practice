years = int(input("Enter number of years: "))

unit = input(input(""" Pick which unit to convert to: 
                1-Days
                2-Weeks
                3-Months
                Input: """))

if unit == 1:
    print(f"{365 * years} days")

elif unit == 2:
    print(f"{52 * years} weeks")

elif unit == 3: 
    print(f"{12 * years} months")    

else: 
    print("Pick the right choice")   