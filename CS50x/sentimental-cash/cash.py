# TODO

from cs50 import get_float

QUATERS = 0.25
DIMES = 0.10
NICKELS = 0.05
PENNIES = 0.01

while True:
    value = get_float("Change owed: ")
    if value > 0:
        break

coins = {"quaters": 0, "dimes": 0, "nickels": 0, "pennies": 0}
rem = value

if rem >= QUATERS:
    coins["quaters"] = int(value / QUATERS)
    rem = rem - coins["quaters"] * QUATERS
    rem = round(rem * 1000) / 1000
if rem >= DIMES:
    coins["dimes"] = int(rem / DIMES)
    rem = rem - coins["dimes"] * DIMES
    rem = round(rem * 1000) / 1000
if rem >= NICKELS:
    coins["nickels"] = int(rem / NICKELS)
    rem = rem - coins["nickels"] * NICKELS
    rem = round(rem * 1000) / 1000
if rem >= PENNIES:
    coins["pennies"] = int(rem / PENNIES)
    rem = rem - coins["pennies"] * PENNIES
    rem = round(rem * 1000) / 1000

result = coins["quaters"] + coins["dimes"] + coins["nickels"] + coins["pennies"]

print(result)
