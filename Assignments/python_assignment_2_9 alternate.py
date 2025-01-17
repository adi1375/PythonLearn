# Task 9: Write a Python program that counts the number of times a particular element occurs in an array list using a loop.

from array import *

integer_array = array("i", [])

n = int(input("Enter number of elements: "))

print(f"Enter {n} numbers:")
for i in range(n):
    integer_array.append(int(input()))


# COUNT FOR SPECIFC USER INPUT
# x = int(input("Enter the number to be searched: "))
# count = 0
# for i in range(n):
#     if x == integer_array[i]:
#         count += 1
# print(f"{x} occurs {count} times.")

# COUNT ALL ELEMENTS AND DISPLAY IN ORDER OF INPUT
count = {}
for i in integer_array:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

print(count)

# COUNT ALL ELEMENTS AND DISPLAY IN ORDERED MANNER
duplicate = {}
for i in set(integer_array):
    duplicate[i] = integer_array.count(i)

print(duplicate)

# COUNT ALL ELEMENTS AND DISPLAY IN ORDERED MANNER WITH TEXT
for key, value in duplicate.items():
    print(f"{key} occurs {value} times.")
