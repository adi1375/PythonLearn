# 1. Create and Access a Dictionary:
# Create a dictionary person with the keys "name", "age", and "city", and assign appropriate values to them.
# Print the value associated with the key "name".
# Expected Output:
# Alice

person = {"name": "Alice", "age": 24, "city": "Wonderland"}
print(f"\nAnswer 1:")
print(person["name"])

# 2. Add and Update Dictionary Entries:
# Start with the dictionary person from the previous exercise.
# Add a new key-value pair "job": "Engineer".
# Update the "age" to 30.
# Print the updated dictionary.
# Expected Output:
# {'name': 'Alice', 'age': 30, 'city': 'Wonderland', 'job': 'Engineer'}

person["job"] = "Engineer"
person["age"] = 30
print(f"\nAnswer 2:")
print(person)

# 3. Dictionary Key-Value Loop:
# Using the person dictionary, print all the key-value pairs in the format "key: value".
# Expected Output:
# name: Alice
# age: 30
# city: Wonderland
# job: Engineer

print(f"\nAnswer 3:")
for key, value in person.items():
    print(f"{key}: {value}")

# 4. Dictionary Membership Test:
# Check if the key "salary" is in the person dictionary.
# Print the result (True or False).
# Expected Output:
# False

print(f"\nAnswer 4:")
print("salary" in person)
