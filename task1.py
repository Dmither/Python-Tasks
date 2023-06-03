from math import pi, sqrt

# 1 ====================

# a = int(input())
# b = int(input())
# c = int(input())

# print(a + b + c)
# print(a * b * c)
# print(a ** (b - c))

# 2 ====================

# a = int(input())
# print(a * 123)

# 3 ====================

# name = input()
# age = int(input())
# hobby = input()
# print("My name is " + name + ". I am " + str(age) + " and my hoddy is " + hobby)

# 4 ====================

# a = float(input())
# b = float(input())
# print('%.2f' % round(a * b / 2, 2))

# 5 ====================

# num = int(input())
# print("The next number for the number", num, "is", num + 1, sep=" ")

# 6 ====================

# num = int(input())
# print(num % 10)

# 7 ====================

# name = input()
# balance = float(input())
# print("Hello,", name, "subscriber! Your current balance is", "%.2f" %
#       round(balance, 2), "UAH")

# 8 ====================

# name = input()
# surname = input()
# print("Hello, " + surname + " " + name + "!")

# 9 ====================

# name = input()
# print("Hello, ", name, "!", sep="")

# 10 ===================

# num = int(input())
# print(2 ** num)

# 11 ===================

# num = int(input())
# print(num // 10)

# 12 ===================

# num = input()
# lst = []
# for i in range(0, len(num), 3):
#     lst.insert(0, num[-1 - i - 3: -1 -i])
# print(",".join(lst))

# 13 ===================

# r = float(input())
# print("{:.3f}".format(round(pi * r ** 2, 3)))

# 14 ===================

# a = int(input())
# b = int(input())
# print("(", a, " + ", b, ") * (", a, " + ", b, ") = ", (a + b) * (a + b), sep="")

# 15 ===================

# feet = float(input("Feet: "))
# inches = float(input("Inches: "))
# height = feet * 30.48 + inches * 2.54
# print("Your height is:", round(height), "cm.")

# 16 ===================

# feet = float(input("input distance in feet: "))
# print("The distance in inches is", round(feet * 12, 3), "inches.")
# print("The distance in yards is", round(feet / 3, 3), "yards.")
# print("The distance in miles is", round(feet * 0.000189393939, 3), "miles.")

# 17 ===================

# symbol = input()
# print(ord(symbol[0]))

# 18 ===================

# num = int(input())
# print(chr(num))

# 19 ===================

# a = int(input())
# b = int(input())
# print(a, "+", b, "=", a+b)

# 20 ===================

# a = int(input())
# b = int(input())
# a, b = b, a
# print(a, b)

# 21 ===================

# num = float(input())
# print("{:.2f}".format(num))

# 22 ===================

# num = input()
# while len(num) < 5:
#     num = "0" + num
# print(num)

# 23 ===================

# num = input()
# while len(num) < 7:
#     num += "*"
# print(num)

# 24 ===================

# num = float(input())
# print("{:.2f}".format(num * 100) + "%")

# 26 ===================

# days = int(input("Days: "))
# hours = int(input("Hours: "))
# minutes = int(input("Minutes: "))
# seconds = int(input("Seconds: "))
# print("The amounts of seconds: " + str(days * 86400 +
#       hours * 3600 + minutes * 60 + seconds) + ".")

# 27 ===================

# f = float(input("Enter the desired future value: "))
# r = float(input("Enter the annual interest rate: "))
# n = int(input("Enter the number of years the money will grow: "))
# for i in range(n):
#     f = (f / (1 + r))
# print("You will need to deposit this amount:", "{:.2f}".format(f))

# 28 ===================

# a = int(input())
# print(a * 1234)

# 29 ===================

# a = input()
# b = input()
# c = input()
# print(c, b, a)

# 30 ===================

# print(int(input()) ** 181)

# 31 ===================

# a = float(input())
# b = float(input())
# print(sqrt(a ** 2 + b ** 2))

# 32 ===================

# a = float(input())
# b = float(input())
# c = float(input())
# p = (a + b + c) / 2
# print(sqrt(p * (p-a) * (p-b) * (p-c)))

# 33 ===================

# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a ** b)

# 34 ===================

# a = int(input())
# b = int(input())
# print((45 + a - 11) / (b - 5) ** 3)

# 35 ===================

# a = int(input())
# b = int(input())
# print((a + b), (a - b), a * b, a / b, a ** b, sep="&")

# 36 ===================

# a = int(input())
# b = int(input())
# print("{:.5f}".format(a / b), "***  ", "{:.5f}".format(b / a), sep="")

# 37 ===================

# a = input()
# b = input()
# c = input()
# print("Points: ", end="")
# print(a, b, c, sep=", ", end=".\n")

# 38 ===================

# a = input()
# print(float(a))
# print(int(float(a)))

# 39 ===================

# num = int(input())
# word = input()
# flt = float(input())
# print(type(num))
# print(type(word))
# print(type(flt))

# 40 ===================

a = float(input())
print("{:.3f}".format(a))