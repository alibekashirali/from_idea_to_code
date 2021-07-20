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
