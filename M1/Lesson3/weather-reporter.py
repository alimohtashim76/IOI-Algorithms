# ********************************
#  MY WEATHER REPORTER
# ********************************


# PART 1 - USER INPUT
city = input("Enter the name of your city: ")
temprature = float(input("Enter today's temperature in Celcius: "))


# PART 2 - if STATEMENT
if temprature > 35:
    print("Warning: It is very hot today!. Please do not go outside.")


# PART 3 - if-else
if temprature > 24:
    print("Great day to go outside!")
else:
    print("Grab a jacket before you go out!")


# PART 4 - if-elif-else
if temprature > 35:
    print("Weather: Scorching Hot")
elif temprature > 25:
    print("Weather: Warm and Sunny")
elif temprature > 15:
    print("Weather: Cool and Breezy")
else:
    print("Weather: Cold - stay warm!")


# PART 5 - datetime MODULE
import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))