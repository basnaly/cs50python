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

if value >= QUATERS:
    coins["quaters"] = int(value / QUATERS)
    rem = value - coins["quaters"] * QUATERS
    # rem = int(rem * 100) / 100
    #print(rem)
if rem >= DIMES:
    coins["dimes"] = int(rem / DIMES)
    rem = rem - coins["dimes"] * DIMES
    # rem = int(rem * 100) / 100
if rem >= NICKELS:
    coins["nickels"] = int(rem / NICKELS)
    rem = rem - coins["nickels"] * NICKELS
    rem = int(rem * 1000) / 1000
if rem >= PENNIES:
    coins["pennies"] = int(rem / PENNIES)
    rem = rem - coins["pennies"] * PENNIES
    rem = int(rem * 1000) / 1000

print(coins)
print(rem)

result = coins["quaters"] + coins["dimes"] + coins["nickels"] + coins["pennies"]

print(result)

