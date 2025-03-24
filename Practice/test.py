# # factorial
# def factorial(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * factorial(num - 1)


# n = int(input("Enter a number: "))

# print(factorial(n))


# ==============================================
# fibonacci f[n] and fibonacci list
# def fibonacci(num):
#     if num <= 1:
#         return num
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)


# n = int(input("Enter a number: "))

# # fibonacci f[n]
# # print(f"Fibonacci F[{n}]: {fibonacci(n)}")

# # fibonacci list n number of terms
# if n == 0:
#     print("Invalid input.")
# for i in range(0, n):
# print(f"{fibonacci(i)}", end=" ")


# ==============================================
# # fibonaci nth term
# def fibonacci(num):
#     if num <= 1:
#         return num
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)


# n = int(input("Enter the number: "))

# print(f"The {n}th Fibonacci term is : {fibonacci(n)}")


# ==============================================
# palindrome string
# def palindrome(text):
#     if text.lower() == text.lower()[::-1]:
#         print("Palindrome")
#     else:
#         print("Not palindrome")


# str = input("Enter some text: ")
# palindrome(str)


# ==============================================
# palindrome number
# def palindrome(num):
#     rev = 0
#     orignal = num
#     while num > 0:
#         temp = num % 10
#         rev = rev * 10 + temp
#         num = num // 10

#     return print(rev == orignal)


# palindrome(12321)
# ==============================================
# max int array
# array = []

# n = int(input("Enter number of elements: "))

# print(f"Enter {n} numbers:")
# for i in range(n):
#     array.append(int(input()))

# print(f"The current array is: {array}")

# max = array[0]

# for i in range(n):
#     if max < array[i]:
#         max = array[i]


# print(f"The largest element is {max}.")
# ==============================================
# def countAlphabets(text):
#     dupe = {}
#     text = text.upper().replace(" ", "")
#     for i in set(text):
#         dupe[i] = text.count(i)

#     # print(dict(sorted(dupe.items(), key=lambda item: item[1], reverse=True)))
#     for key, value in sorted(dupe.items()):
#         print(f"{key} occurs {value} times.")


# countAlphabets("aljsdhfnlayhwddelnfhlakynljhjbylefkaef")
# ==============================================
# hcf,lcm
# def hcf(a, b):
#     if b == 0:
#         return a
#     return hcf(b, a % b)


# print(hcf(36, 60))


# def lcm(a, b):
#     return a * b // hcf(a, b)


# print(lcm(36, 60))
# ==============================================

# swap numbers
# def swap(a, b):
#     a = a + b
#     b = a - b
#     a = a - b
#     return (a, b)


# print(swap(9, 16))
# ==============================================

# prime
# def prime(n):
#     if n <= 1:
#         print(f"{n} in neither prime nor composite.")
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True


# print(prime(10))
# ==============================================

# largest prime factor
# def largestPrimefactor(n):
#     largest = -1

#     while n % 2 == 0:
#         largest = 2
#         n //= 2

#     i = 3
#     while i * i <= n:
#         while n % i == 0:
#             largest = i
#             n //= i
#         i += 2
#     if n > 2:
#         largest = n

#     return largest


# print(largestPrimefactor(25))
# def leapYear(n):
#     return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)


# print(leapYear(2024))
# ==============================================
# Armstrong number
# def armstrongNumber(num):
#     n = num
#     str_num = str(num)
#     power = len(str_num)
#     sum = 0
#     # for i in str_num:
#     #     sum += int(i) ** power
#     # return sum == num

#     while n != 0:
#         r = n % 10
#         sum += r**power
#         n //= 10
#     return sum == num


# print(armstrongNumber(153))
# ==============================================
Shots = {
    "C": "Counter Drive",
    "D": "Drive",
    "H": "Hook Shot",
    "S": "Straight Drive",
    "P": "Pull Drive",
}
str = "SSSSPPPPHHHH"
c = ""
counter = 0
dictionary = {}

for i in str:
    if i == c:
        counter += 1
        if i in dictionary:
            if counter > dictionary[i]:
                dictionary[i] = counter
    else:
        counter = 1
        if i not in dictionary:
            dictionary.update({i: counter})
        c = i


print(dict(sorted(dictionary.items())))

max = max(dictionary.values())
max2 = 0
result = None
for k, v in sorted(dictionary.items()):
    if v > max2 and v < max:
        max2 = v
        result = k
    if result == None:
        result = next(iter(sorted(dictionary)))
if result in Shots:
    print(Shots[result])
