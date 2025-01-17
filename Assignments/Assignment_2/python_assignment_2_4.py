# Task 4: Write a Python program that counts the number of vowels in a given string using a for loop and an if statement.

from array import *

text = input("Enter some text: ")

vowels = 0

for i in range(len(text)):
    if (
        text[i] == "a"
        or text[i] == "e"
        or text[i] == "i"
        or text[i] == "o"
        or text[i] == "u"
        or text[i] == "A"
        or text[i] == "E"
        or text[i] == "I"
        or text[i] == "O"
        or text[i] == "U"
    ):
        vowels += 1
print(f"The number of vowels in the text is {vowels}.")

vowels_array = array("u", ["a", "e", "i", "o", "u"])

vowels = 0
for i in range(len(text)):
    for char in vowels_array:
        if ord(text[i]) == ord(char) or ord(text[i]) == ord(char) - 32:
            vowels += 1

print(f"The number of vowels in the text is {vowels}.")
