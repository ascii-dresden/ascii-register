import datetime
# Script for counting money for ascii Dresden.
# This is definitely no well written python. One of my first little projects. 

name = "Julius Felchow"

"""
Array that contains the values of bills and coins.
"""
staggering = [100, 50, 20, 10, 5, 2, 1, .5, .2, .1, .05, .02, .01]
"""
Arrays for amounts of the bills and coins.
"""
amounts = [0 for i in range(13)]
proposed_amounts = [0 for i in range(13)]

"""
Integers for money amount.

```total``` is the sum of all the money in the register.
```rest``` is the sum of the money that should be put into the envelope.
```register_money``` is the sum of the money that should remain in the register.
"""
total = 0
rest = 0
register_money = 0

def dev_values(amounts) :
    """Sets arbitrary values for amounts for testing."""
    # values for development
    amounts[0] = 1
    amounts[1] = 2
    amounts[2] = 4
    amounts[3] = 8
    amounts[4] = 9
    amounts[5] = 14
    amounts[6] = 28
    amounts[7] = 23
    amounts[8] = 32
    amounts[9] = 33
    amounts[10] = 16
    amounts[11] = 7
    amounts[12] = 2

def read_input(amounts) :
    """Reads the input for the amount of bills and coins in the register."""
    try:
        amounts[0] = int(input('Amount 100: '))
        amounts[1] = int(input('Amount  50: '))
        amounts[2] = int(input('Amount  20: '))
        amounts[3] = int(input('Amount  10: '))
        amounts[4] = int(input('Amount   5: '))
        amounts[5] = int(input('Amount   2: '))
        amounts[6] = int(input('Amount   1: '))
        amounts[7] = int(input('Amount  .5: '))
        amounts[8] = int(input('Amount  .2: '))
        amounts[9] = int(input('Amount  .1: '))
        amounts[10] = int(input('Amount .05: '))
        amounts[11] = int(input('Amount .02: '))
        amounts[12] = int(input('Amount .01: '))
    except ValueError:
        print("NaN")

def calculate_staggering():
    """
    Calculates a proposed staggering for the amount of bills and coins that should be put into the counter.

    Definitely not fail proof and not intelligent yet. 
    Adjust the staggering to keep in 5 and 10 Euro bills.
    """
    proposed_amounts[10] = amounts[10]
    proposed_amounts[11] = amounts[11]
    proposed_amounts[12] = amounts[12]
    for i in range(amounts[0]):
        if get_overlap() >= staggering[0]:
            proposed_amounts[0] += 1
    for i in range(amounts[1]):
        if get_overlap() >= staggering[1]:
            proposed_amounts[1] += 1
    for i in range(amounts[2]):
        if get_overlap() >= staggering[2]:
            proposed_amounts[2] += 1
    for i in range(amounts[3]):
        if get_overlap() >= staggering[3]:
            proposed_amounts[3] += 1
    for i in range(amounts[4]):
        if get_overlap() >= staggering[4]:
            proposed_amounts[4] += 1
    for i in range(amounts[5]):
        if get_overlap() >= staggering[5]:
            proposed_amounts[5] += 1
    for i in range(amounts[6]):
        if get_overlap() >= staggering[6]:
            proposed_amounts[6] += 1
    for i in range(amounts[7]):
        if get_overlap() >= staggering[7]:
            proposed_amounts[7] += 1
    for i in range(amounts[8]):
        if get_overlap() >= staggering[8]:
            proposed_amounts[8] += 1
    for i in range(amounts[9]):
        if get_overlap() >= staggering[9]:
            proposed_amounts[9] += 1

def get_overlap():
    """Calculates the overlap, that is still too much in the register for the proposed staggering."""
    proposed = 0
    for i in range(0,13):
        proposed += proposed_amounts[i] * staggering[i]
    return round(total - proposed - 100, 2)

read_input(amounts)
#dev_values(amounts)

print("\nValues for table: " + str(amounts) + "\nCheck these again, to be sure you didn't make a typo.\n")

for i in range(0,13):
    total += amounts[i] * staggering[i]

total = round(total, 2)

register_money = total - 100

calculate_staggering()


print("Sum: " + str(total))
print("Rest in register: " + str(total - register_money)) # adjust later
print("\nProposed staggering:\nAmount 100: " + str(proposed_amounts[0]) + "\nAmount  50: " + str(proposed_amounts[1]) + "\nAmount  20: " + str(proposed_amounts[2]) + "\nAmount  10: " + str(proposed_amounts[3]) + "\nAmount   5: " + str(proposed_amounts[4]) + "\nAmount   2: " + str(proposed_amounts[5]) + "\nAmount   1: " + str(proposed_amounts[6]) + "\nAmount  .5: " + str(proposed_amounts[7]) + "\nAmount  .2: " + str(proposed_amounts[8]) + "\nAmount  .1: " + str(proposed_amounts[9]) + "\nAmount .05: " + str(proposed_amounts[10]) + "\nAmount .02: " + str(proposed_amounts[11]) + "\nAmount .01: " + str(proposed_amounts[12]))

now = datetime.datetime.now()
print("\nInscription for envelope:\nName     " + name + "\nDate     " + str(now.day) + "." + str(now.month) + "." + str(now.year))
print("Money    " + str(round(total - 100, 2)))
