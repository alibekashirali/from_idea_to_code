#1 Calculator

first = int(input("Введите первое число\n"))
operand = input("Что нужно сделать?\n")
second = int(input("Введите второе число\n"))
res = 0

if operand == "+":
	res = first + second
elif operand == "-":
	res = first - second
elif operand == "*":
	res = first * second
elif operand == "/":
	res = first / second
elif operand == "//":
	res = first // second
elif operand == "**":
	res = first ** second
elif operand == "%":
	res = first % second
else:
	print("Введена не правильная операция")
	res = "-"

print(f"Результат равен: {res}")


#2 divided apples

n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))

print("Сейчас будет магия")
print(f"Вывод: {k // n}, остаток: {k % n}")


#3 night club

sex = input("Введите пол (f или m): ")
if sex != "m" or sex != "f":
	flag = True
	while flag:
		sex = input("Введите нормальный пол: ")
		if sex == "m" or sex == "f":
			flag = False

age = int(input("Введите возраст: "))

if (sex == "f" and age >= 18) or (sex == "m" and age >= 21):
	print("добро пожаловать")
else:
	print("вход запрещен")


#4 random numbers

import random

num = random.randrange(100, 1000)
num = str(num)
a = 0
b = 1

for i in num:
	a += int(i)
	b *= int(i)

print(f"Число: {num}  Сумма: {a}  Произведение: {b}")



