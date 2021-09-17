what = input("Выбери действие(+,-,/,*):")

a = float ( input ("Первое число:") )
print (a)
b = float ( input ("Второе число:") )
print (b)
if what == "+" :
	c = a + b
	print ("Результат:" + str(c) )
if what == "-" :
	c = a - b
	print ("Результат:" + str(c) )
if what == "/":
	c = a / b
	print ("Результат:" + str(c) )
if what == "*" :
	c = a * b
	print ("Результат:" + str(c) )	
elif c < 100 :
	print("Маленькое число")
elif c > 100
	print ("Большое число")