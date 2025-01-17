# 1.Create a List:
# Create a list called fruits containing the following items: "apple", "banana", "cherry".
# Add "orange" to the end of the list.
# Insert "mango" between "banana" and "cherry".
# Remove "banana" from the list.
# Print the final list.
# Expected Output:
# ['apple', 'mango', 'cherry', 'orange']


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(2, "mango")
fruits.remove("banana")
print(f"\nAnswer 1:")
print(fruits)

# 2.Accessing and Modifying List Elements:
# Create a list of integers from 1 to 5.
# Replace the number 3 with 10.
# Print the updated list.
# Expected Output:
# [1, 2, 10, 4, 5]

num_list = list(range(1, 6))
i = num_list.index(3)
num_list[i] = 10
print(f"\nAnswer 2:")
print(num_list)

# 3.List Slicing:
# Given a list numbers = [10, 20, 30, 40, 50, 60], extract the sublist containing the middle three elements.
# Print the sublist.
# Expected Output:
# [30, 40, 50]

num_list = [10, 20, 30, 40, 50, 60]
print(f"\nAnswer 3:")
print(num_list[2:5])

# 4. List Sorting:
# Create a list of numbers [4, 1, 7, 3, 8, 2].
# Sort the list in descending order and print it.
# Expected Output:
# [8, 7, 4, 3, 2, 1]

num_list = [4, 1, 7, 3, 8, 2]
print(f"\nAnswer 4:")
# num_list.sort(reverse=True)
print(sorted(num_list, reverse=True))
