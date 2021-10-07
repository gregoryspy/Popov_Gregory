print ("Ноль в качеств знака \nоперации завершит работу")
what = input("Выбери действие(+,-,/,*):")
if what == 0 :
    break
a = float ( input ("Первое число:") )
print (a)
b = float ( input ("Второе число:") )
print (b)

elif what == "+" :
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
elif c > 100 :
    print ("Большое число")
else :
    print ("Неверный знак операции!")