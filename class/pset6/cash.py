import cs50
import math

dollars = cs50.get_float("Change owed: ")
while dollars < 0:
    dollars = cs50.get_int("Change owed: ")
cents = round(dollars * 100)
q = (int)(cents / 25.0)
quater = cents - 25.0*q
d = (int)(quater / 10.0)
dime = quater - 10.0*d
n = (int)(dime / 5.0)
nickel = dime - 5.0*n
p = (int)(nickel / 1.0)
penny = nickel - 1.0*p

coins = q + d + n + p
print(f"{coins}")
