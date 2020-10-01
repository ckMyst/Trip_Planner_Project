'''
Connor Kissack
9/24/2020
Trip Planner Assignment
'''

# time_difference = int(input("What is the time difference, in hours, between your home and your destination? If the time is behind, use a negative symbol in front of the amount of hours. ") #our_time_input = 12
# Part 1: Make A Greeting
print("Welcome to Vacation Planner")
customers_name = input("What's your name?")
destination = input("Nice to meet you " + customers_name+" where are you travelling to?")
print("Great! "+ destination + " Sounds like a great trip!")
print("*.+.*.+.*.+.*.+.*.+.*.+.*")
print(' ')
number_of_days = int(input("How many days are you going to spend travelling?"))
integer_number_of_days = int(number_of_days)
budget = int(input('How much money are you going to be spending on this trip? '))
currency = input('What is the three letter currency symbol for your destination?')
conversion_rate = float(input('How many MXC are there in 1 USD?'))
print("*.+.*.+.*.+.*.+.*.+.*.+.*")
print(' ')
# Part 2: Travel time and budget
hours = number_of_days * 24
minutes = hours * 60
print(f'If you are travelling for {number_of_days} days this is the same as {hours} hours or {minutes} minutes')
daily_budget = budget / number_of_days
print(f'If you are going to spend {budget} {currency} that means you are going to spend up to {daily_budget} {currency}')
print("O-*_.+.*._+.*.+._*_.+.*.+_.*.+._*-O")
print(' ')
noon = 12
midnight = 0
time_difference = int(input('What is the time difference, in hours, in between your home and your destination? '))
adjusted_midnight = time_difference + midnight
adjusted_noon = time_difference + noon
midnight_msg = f'That means that when it is midnight where you live it will be {adjusted_midnight} in your travel destination'
noon_msg = f'and when it is noon where you live it will be {adjusted_noon}'
if time_difference <= 24 and time_difference >= 0:

if(time_difference < -12):
    adjusted_midnight = 24+time_difference
    print(f'That means what when it is midnight at home it will be {adjusted_midnight} in the previous day in your travel destination')
    print(f'and when it is noon at home it will be {adjusted_noon}')


def time_change():
    time_difference = int(input('What is the time difference, in hours, in between your home and your destination? '))
    noon = 12
    midnight = 0
    # so the time difference could be + or
    # convert the string to a int
    int_time_difference = int(time_difference)

    # calculate from noon
    difference_hrs_noon = noon + int_time_difference
    difference_hrs_midnight = midnight + int_time_difference
    print(difference_hrs_noon,"Difference Hours Noon", difference_hrs_midnight, "Difference Hours Midnight")
    # these two conditions are on different days
    # use % to get how many hours over into the next day could be + or -
    adjusted_noon = difference_hrs_noon%24
    adjusted_midnight = difference_hrs_midnight%24
    print(adjusted_noon, "This number is the adjusted hours for noon")
    print(adjusted_midnight, "This is the adjusted hours for midnight")
    if difference_hrs_noon <= 24 and difference_hrs_noon >= 0:
        print("Destination time is ", difference_hrs_noon, ":00 from noon 12:00")
    if difference_hrs_noon > 24:
        print(f"Destination time is  {adjusted_noon}:00 hr(s) on the next day from noon 12:00")
    if difference_hrs_noon < 0:
        print(f"Destination time is  {adjusted_noon}:00 hr(s) on the previous day from noon 12:00")


    if difference_hrs_midnight <= 24 and difference_hrs_midnight >= 0:
        print("Destination time is ", difference_hrs_midnight, ":00 from noon 0:00")
    if difference_hrs_midnight > 24:
        print(f"Destination time is  {adjusted_midnight}:00 hr(s) on the next day from midnight 0:00")
    if difference_hrs_midnight < 0:
        print(f"Destination time is  {adjusted_midnight}:00 hr(s) on the previous day from midnight 0:00")

time_change()







