# 1. Create and Access a Tuple:
# Create a tuple named colors containing "red", "green", and "blue".
# Print the second color in the tuple.
# Expected Output:
# green

colours = ("red", "green", "blue")
print(f"\nAnswer 1:")
print(colours[1])

# 2. Tuple Unpacking:
# Create a tuple dimensions = (1920, 1080).
# Unpack the values into two variables width and height.
# Print the values of width and height.
# Expected Output:
# Width: 1920, Height: 1080

dimensions = (1920, 1080)
width, height = dimensions
print(f"\nAnswer 2:")
print(f"Width: {width}, Height: {height}")

# 3. Tuple Concatenation:
# Create two tuples: odd_numbers = (1, 3, 5) and even_numbers = (2, 4, 6).
# Concatenate these tuples into a single tuple all_numbers.
# Print all_numbers.
# Expected Output:
# (1, 3, 5, 2, 4, 6)

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)
all_numbers = odd_numbers + even_numbers
print(f"\nAnswer 3:")
print(all_numbers)

# 4. Tuple Membership Test:
# Given a tuple names = ("Alice", "Bob", "Charlie"), check if "Charlie" is in the tuple.
# Print the result (True or False).
# Expected Output:
# True

names = ("Alice", "Bob", "Charlie")
print(f"\nAnswer 4:")
print("Charlie" in names)
