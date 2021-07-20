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


#2 delenie
a = int(input("Введите число: "))
b = int(input("Введите делитель: "))

if a % b == 0:
	print("Делится")
else:
	print("Не делится")


#3 password
a = input("Введите пароль: ")
b = input("Введите ещё раз: ")

if a == b:
	print("Пароль принят")
else:
	print("Пароль не принят")



#4 divided apples
n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок: "))

print("Сейчас будет магия")
print(f"Вывод: {k // n}, остаток: {k % n}")


#5 race
n = int(input("Скорост Зума: "))
k = int(input("Скорост Флэша: "))

if n > k:
	print("NO")
elif n < k:
	print("Yes")
else:
	print("Don't know")


#6 min of numbers
num = input("Введите сразу четыре числа через пробел: ")

array = num.split(' ')
a = 0
n = len(array)

for k in range(n):
	array[k] = int(array[k])

for i in range(n-1):
	for j in range(n-i-1):
		if array[j] > array[j+1]:
			array[j], array[j+1] = array[j+1], array[j]

print(array[0])


#7 weight of fighters
weight = int(input("Введите вес: "))

if weight < 60:
	print("Легкий вес")
elif weight >= 60 and weight < 64:
	print("Первый полусредний вес")
elif weight >= 64 and weight < 69:
	print("Полусредний вес")
else:
	print("Такой весовой категории нет")


#8 night club
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


#9 random numbers
import random

num = random.randrange(100, 1000)
num = str(num)
a = 0
b = 1

for i in num:
	a += int(i)
	b *= int(i)

print(f"Число: {num}  Сумма: {a}  Произведение: {b}")


#10 colors of wheel
num = int(input("Введите число: "))

def even(x):
	if x % 2 == 0:
		return True
	else:
		return False

if num == 0:
	print("Зеленый")
elif num >= 1 and num <= 10:
	if even(num):
		print("Черный")
	else:
		print("Красный")
elif num >= 11 and num <= 18:
	if even(num):
		print("Красный")
	else:
		print("Черный")
elif num >= 19 and num <= 28:
	if even(num):
		print("Черный")
	else:
		print("Красный")
elif num >= 29 and num <= 36:
	if even(num):
		print("Красный")
	else:
		print("Черный")
else:
	print("ошибка ввода")
