#!python3
"""
Assignment: Exchange rate
The current exchange rate is 1.25 CAD per 1 USD
Create a program that asks the user for the number of Canadian Dollars they have
and then have the program display how many USD that is equivalent to:
You may need to use rounding or decimal formatting


example
How many Canadian Dollars do you have? 10
That is worth $8.00 USD

How many Canadian Dollars do you have? 1.25
That is worth $1.00 USD
"""
current_population = int(input("Enter the population"))
r= float(input("Enter the rate of growth in percent"))
time = int(input("Enter the number of days"))
rw = r/100
population = current_population*(1+rw)**(time/365)
pop = round(population)
print(f"There will be {pop} people after {time} days")