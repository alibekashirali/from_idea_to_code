#WEEK 3

#1 Type of data in python

# list: ordered, changeable, allow duplicates
# tuple: ordered, changeable, allow duplicates
# set: not ordered, changeable, not allow duplicates 
# dict: ordered, not changeable, not allow duplicates


#2 sort words
a = "HELLO I AM WRITING CODE"

array = a.split(' ')
array.sort()
print(array)


#3 programer
array = ["Алибек", "Женя", "Бека", "Дана"]

for i in array:
	print(f"{i} программист")


#4 words txt
file = open("words.txt", "w")

for i in range(1000):
	file.write("I am developer\n")

file.close()


#5 list: element less than 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
	if i < 5:
		print(i, end = " ")

#6 common numbers
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 

c = list(set(a).intersection(b))
print(c)


#7 number: 237
a = [2,3,4,7,237,2,2,4]

for i in a:
	if (i%2) == 0 and i != 237:
		print(i, end = " ")
	elif i == 237:
		break


#8 how many symbols
a = input("Введите текст: ")
b = input("Введите символ: ")
count = 0

for i in a:
	if b == i:
		count += 1

print(f"символ {b} встречается {count} раза")


#9 unqie or not function
a = [int(x) for x in input().split()]

def unique_or_not(x):
	arr = set(x)
	if len(arr) == len(x):
		return True
	else:
		return False

print(unique_or_not(a))


#10 two words
text = input()

def quan(array):
	for i in array:
		for k in range(1, )

array = text.split()
arr = [] 

for i in array:
	arr.append(len(i))


#11 two random numbers
import random

num = random.randrange(100, 1000)
num = str(num)
a = 0
b = 1

for i in num:
	a += int(i)
	b *= int(i)

print(f"Число: {num}  Сумма: {a}  Произведение: {b}")


#12 game random numbers
num = random.randrange(1, 51)

for i in range(3):
	a = int(input("Введите число: "))
	if num > a:
		print("больше")
	elif a > num:
		print("меньше")
	elif a == num:
		print("В точку")
		break


#13 game random numbers
a = input("Введите числа через пробел: ")

a = a.split()
b = set(a)

c = len(a) - len(b)
if len(b) == 1:
	c = c + 1
print(c)


#14 text with "_"
text = input("Введите текст: ")

array = text.split(' ')

a = ""

for i in array:
	a += i + "_"

print(a)


# 15 count unique numbers
list1 = [int(x) for x in input("Числа через пробел: ").split(' ')]

nums = set(list1)
data = dict()

for i in nums:
	data.update({i: list1.count(i)})

print(data)


#16 sum and multiply of numbers
from random import randrange
numbers = [int(x) for x in input().split(' ')]

def sum(num):
	a = randrange(2)
	b = 0
	if a == 0:
		for i in num:
			b += i
		return b
	elif a == 1:
		c = 0
		while c < len(num):
			b += num[c]
			c += 1
		return b

def multiply(num):
	a = randrange(2)
	b = 1
	if a == 0:
		for i in num:
			b *= i
		return b
	elif a == 1:
		c = 0
		while c < len(num):
			b *= num[c]
			c += 1
		return b

print(sum(numbers))
print(multiply(numbers))


# #17 max number
a = input("число 1: ")
b = input("число 2: ")

c = a + b
d = b + a

print(max(int(c), int(d)))


#18 calendar
date = int(input("Введите дату: "))

if date % 4 != 0 or (date % 100 == 0 and date % 400 != 0):
	print("Не високосный")
else:
	print("Високосный")


#19 listdir with os
from os import listdir

list_dir = listdir()

for i in list_dir:
	print(i)


#20 file format
name = input("Введите имя файла: ")

def fileformat(filename):
	parts = filename.split('.')
	try:
		first, end = parts
		return parts[-1]
	except:
		print("Файл не имеет расширения")

print(fileformat(name))


#20 calculator
a = input("Введите число1, оператор и число2 через пробел: ").split()

def calculator(num1, operand, num2):
	try:
		if operand == "+":
			c = num1 + num2
		elif operand == "-":
			c = num1 - num2
		elif operand == '*':
			c = num1 * num2
		elif operand == '/':
			c = num1 / num2
		elif operand == '**':
			c = num1 ** num2
		elif operand == '%':
			c = num1 % num2
		else:
			c = "Неправильное значение"
		if c > int(c):
			return float(c)
		else:
			return int(c)
	except:
		print("какая-то ошибка")

try:
	num1, operand, num2 = a
	num1, num2 = float(num1), float(num2)
	print(calculator(num1, operand, num2))
except:
	print("что-то не работает")
