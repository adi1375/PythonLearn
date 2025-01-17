# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_num = int(input("Enter max number: "))
odd_num_list = []
for i in range(1, max_num):
    if i % 2 != 0:
        odd_num_list.append(i)
print(f"List of odd numbers till max number: {odd_num_list}")
