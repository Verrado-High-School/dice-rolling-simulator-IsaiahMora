# Name: Isaiah Mora
# Period: 2

# Dice Rolling Simulator

import random

r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0
r6 = 0

rolls = 1

number = int(input("How many rolls? "))

while rolls <= number:
    roll = random.randint(1, 6)
    if roll == 1:
        r1 += 1
    if roll == 2:
        r2 += 1
    if roll == 3:
        r3 += 1
    if roll == 4:
        r4 += 1
    if roll == 5:
        r5 += 1
    if roll == 6:
        r6 += 1
    print(str(rolls) + ": " + str(roll))
    rolls += 1

print("Total Rolls:")
print("1: " + str(r1))
print("2: " + str(r2))
print("3: " + str(r3))
print("4: " + str(r4))
print("5: " + str(r5))
print("6: " + str(r6))

print("Percentages:")
print("1: " + str(r1 / number * 100))
print("2: " + str(r2 / number * 100))
print("3: " + str(r3 / number * 100))
print("4: " + str(r4 / number * 100))
print("5: " + str(r5 / number * 100))
print("6: " + str(r6 / number * 100))