#week 1 part 2

#1
a = "2.1"
b = "1.04"
pi = float(a) + float(b)

print(pi)


#2
a = "Hello"
b = 123
c = 0
d = -1
f = "-1"

for i in a, b, c, d, f:
	print(bool(i))


#3
word = "«I***like***Python»"
print(word[1:18], sep='\n')

#4
# необязательный парамент sep вставляет значение типа запятой или точки, смотря что мы укажем,  между разными переменными. по дефолту идет sep = ''
# а параметр end вставляет в конце последней переменной

#5
# s = -50

#6
numbers = input()

def calc(num):
	array = num.split(' ')
	a = 0
	for i in array:
		a += int(i)
	print(a * 3)

calc(numbers)


#7

b = input("Введите число: ")

def program(a):
	d = a - 1
	f = a + 1
	a, d, f = str(a), str(d), str(f)

	print("Следующее за числом {} число: {}".format(a, f) )
	if int(a) > 0:
		print("Для числа {} предыдущее число: {}".format(a, d) )

program(int(b))



