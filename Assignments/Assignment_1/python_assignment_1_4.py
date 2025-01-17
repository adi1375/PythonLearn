# 4. Create a program that prints the numbers from 1 to 100,
# but for multiples of 3, print "Fizz" instead of the number,
# and for multiples of 5, print "Buzz".
# For numbers that are multiples of both 3 and 5, print "FizzBuzz".
# repeated that number of times.

n = 20

for i in range(1, n + 1):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"

    if result == "":
        result += str(i)

    print(result)
