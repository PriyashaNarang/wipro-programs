# MINI PROJECT
"""1.	create a python program that asks the user how far they want to travel. if they want to travel less than three miles tell them to ride Bicycle. if they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle. if they want to travel three hundred miles or more tell them to driver Super-Car.
Sample Output:
How far would you like to travel in miles? 2500
I suggest Super-Car to your destination """

dist=int(input("How far would you like to travel in miles? "))
if dist>=0 and dist<3:
    print("I suggest Bicycle to your destination")
elif dist>3 and dist<300:
    print("I suggest Motor-cycle to your destination")
elif dist>=300:
    print("I suggest Super-Car to your destination")
else:
    print("Invalid miles value")

"""2. Let's assume you are planning to use your python skills to build an App for Mobile.
You decide to host your application on servers running in the cloud. you pick a hosting provider that charges $0.51 per hour. you will launch your services using one server and want to know how much it will cost to operate per day, per week, per month.
Write a python program that displays the answers to the following questions:
How much does it cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How much days can I operate one server with $918? """

VAL=0.51
day_val=VAL*24
week_val=day_val*7
month_val=day_val*30
no_of_days=int(918//day_val)
print(f"Cost to operate one server per day: ${day_val}")
print(f"Cost to operate one server per week: ${week_val}")
print(f"Cost to operate one server per month: ${month_val}")
print(f"Days I can operate one server with $918: {no_of_days}")