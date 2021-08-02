#1 changing variables without third variable

a = 5
b = 10

a, b = b, a


#2 reverse time
h = int(input("Введите часы: "))
m = int(input("Введите минуты: "))

if h > 12 or h < 0:
	print("Неправильный час")
elif m > 60 or m < 0:
	print("Неправильная минута")
else:
	x = 12 - h
	y = 60 - m
	if x == 12:
		x = 0
	elif y == 60:
		y = 0
	print(x, y)


#3 checkmate
a = [int(x) for x in input("Введите числа через пробел: ").split()]

if len(a) < 4:
	print("Вы ввели недостаточно данных")
elif max(a) > 8:
	print("Вы ввели значение больше 8")
else:
	if a[0] == a[2] or a[0] == a[2]:
		print("YES")
	elif a[1] == a[2] or a[1] == a[3]:
		print("YES")
	else:
		print("NO")


#4 max number
nums = [x for x in input("Введите числа через пробел: ").split()]

a, b = nums[0] + nums[1] + nums[2], nums[1] + nums[0] + nums[2]
c, d = nums[0] + nums[2] + nums[1], nums[1] + nums[2] + nums[0]
e, f = nums[2] + nums[1] + nums[0], nums[2] + nums[0] + nums[1]

array = [a, b, c, d, e, f]

print(max(array))
