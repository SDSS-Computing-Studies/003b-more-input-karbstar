#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

w = float(input("Enter the first price"))
e = float(input("Enter the second price"))
r = float(input("Enter the third price"))
t = float(input("Enter the fourth price"))
y = float(input("Enter the fift price"))

t1 = w*0.12
t2 = e*0.12
t3 = r*0.12
t4 = t*0.12
t5 = y*0.12

tax = t1 + t2 + t3 + t4 + t5
total = w + e + r + t + y
final = total + tax
print(f"total without tax: {total}" )
print(f"total tax: {tax}")
print (f"final total {final}")