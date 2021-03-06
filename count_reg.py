#!/usr/bin/python3

import datetime
# Script for counting money for ascii Dresden.
# This is fairly well written python. One of my first little projects.

name = "MyName"

# Array that contains the values of bills and coins.
staggering = [100, 50, 20, 10, 5, 2, 1, .5, .2, .1, .05, .02, .01]

# Arrays for amounts of the bills and coins.
amounts = {coin: 0 for coin in staggering}
proposed_amounts = {coin: 0 for coin in staggering}

"""
Integers for money amount.

```total``` is the sum of all the money in the register.
```rest``` is the sum of the money that should be put into the envelope.
```register_money``` is the sum of the money that should remain in the register.
"""
total = 0
rest = 0
register_money = 0


def read_input(amounts : list):
    """Reads the input for the amount of bills and coins in the register."""

    for coin in staggering:
        try:
            amounts[coin] = int(input('Amount {}: '.format('{:6.2f}'.format(coin))))
        except ValueError:
            print("NaN")


def calculate_staggering():
    """
    Calculates a proposed staggering for the amount of bills and coins that should be put into the counter.

    Definitely not fail proof and not intelligent yet.
    Adjust the staggering to keep in 5 and 10 Euro bills.

    A little intelligent yet still dumb.
    """

    # Coins which are always put away
    for coin in staggering[10:]:
        proposed_amounts[coin] = amounts[coin]

    for coin, amount in amounts.items():
        for i in range(amount):
            if get_overlap() >= coin:
                proposed_amounts[coin] += 1


def get_overlap():
    """Calculates the overlap, that is still too much in the register for the proposed staggering."""
    proposed = 0
    for coin in staggering:
        proposed += proposed_amounts[coin] * coin
    return round(total - proposed - 100, 2)

def improve_staggering():
    """If there are no 5 euro bills left in the register, adjust the proposed_amounts."""

read_input(amounts)

print("\nValues for table:")
print(*amounts.values(), sep=', ')
print("Check these again, to be sure you didn't make a typo.\n")

# Calculate coin amount value
for coin in staggering:
    total += amounts[coin] * coin

total = round(total, 2)
register_money = total - 100
calculate_staggering()


print("Sum: " + str(total))
print("Rest in register: " + str(total - register_money))
print("\nProposed staggering for the envelope:")
for coin, amount in proposed_amounts.items():
    print("Amount {}: {}".format("{:6.2f}".format(coin), amount))
print("Make sure there are about 30 euros in bills in the register.")

now = datetime.datetime.now()
print("\nInscription for envelope:\nName     " + name)
print("Date     " + now.strftime("%d.%m.%Y"))
print("Money    " + str(round(total - 100, 2)))
