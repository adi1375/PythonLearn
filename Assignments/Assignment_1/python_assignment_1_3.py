# 3. Create a program that asks the user for a string and a number, 
# and then prints the string. Write a program that asks the user for 
# a number and prints whether it's positive, negative, or zero.

str=input("Enter some text: ")
num=int(input("Enter an integer: "))

print(str)
print(f'The number is {'zero' if num == 0 else 'positive' if num > 0 else 'negative'}')
