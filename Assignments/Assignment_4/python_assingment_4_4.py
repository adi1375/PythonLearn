# 1. Create and Modify a Set:
# Create a set called animals containing "cat", "dog", "bird".
# Add "fish" to the set.
# Remove "dog" from the set.
# Print the final set.
# Expected Output:
# {'cat', 'bird', 'fish'}

animals = {"cat", "dog", "bird"}
animals.add("fish")
animals.remove("dog")
print(f"\nAnswer 1:")
print(animals)

# 2. Set Operations:
# Create two sets: set_a = {1, 2, 3, 4} and set_b = {3, 4, 5, 6}.
# Find the union of the two sets and print it.
# Find the intersection of the two sets and print it.
# Expected Output:
# Union: {1, 2, 3, 4, 5, 6}
# Intersection: {3, 4}

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"\nAnswer 2:")
print(f"Union: {set_a.union(set_b)}")
print(f"Intersection: {set_a.intersection(set_b)}")

# 3. Set Difference:
# Using the sets set_a and set_b from the previous exercise, find the difference between set_a and set_b and print it.
# Expected Output:
# Difference: {1, 2}

print(f"\nAnswer 3:")
print(f"Difference: {set_a.difference(set_b)}")

# 4. Set Membership Test:
# Check if the number 5 is in set_a.
# Print the result (True or False).
# Expected Output:
# False

print(f"\nAnswer 4:")
print(5 in set_a)
