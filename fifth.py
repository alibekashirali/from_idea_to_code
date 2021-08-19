import openpyxl
from random import random

wb = openpyxl.Workbook()

sheet =  wb.active

sheet["A1"].value = "Column_1"
sheet["B1"].value = "Column_2"
sheet["C1"].value = "Column_3"

for i in range(2, 1001):
	a = int((random() * 100))
	b = int((random() * 100))
	sheet[i][0].value = a
	sheet[i][1].value = b
	sheet[i][2].value = (a * b) + a

wb.save(filename = "excel_file.xlsx")

wb.close
