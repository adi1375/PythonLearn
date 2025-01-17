expenses = [2200, 2350, 2600, 2130, 2190]

print(
    f"1. In Feb, how many dollars you spent extra compare to January?\nAns = {expenses[1]-expenses[0]}"
)
print(
    f"2. Find out your total expense in first quarter (first three months) of the year.\nAns = {expenses[0]+expenses[1]+expenses[2]}"
)
print(f"3. Find out if you spent exactly 2000 dollars in any month. {2000 in expenses}")
# counter = 0
# for i in range(len(expenses)):
#     if expenses[i] == 2000:
#         counter += 1
# if counter > 0:
#     print("Yes, Exactly 2000 was spent.")
# else:
#     print("No. Exactly 2000 was not spent.")

print(
    f"4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list."
)
expenses.append(1980)
print(expenses)
print(
    f"5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this."
)
expenses[3] = expenses[3] - 200
print(expenses)
