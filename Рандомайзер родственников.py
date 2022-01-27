import random 
g5=random.randint (1,10)
g6=random.randint (1,10)
g7=random.randint (1,10)
g8=random.randint (1,10)

#Родина персонажа
Name = input("Нажмите Enter выпадет случайные характеристики родственника") 


#Возраст
if g6>=1 and g6<=5 :
	print("Младше вас")
elif g6>=6 and g6<=9:
	print("Старше вас")
elif g6==10:
	print("Ваш близнец")
else:
	print
#как к вам относиться 
print("Как отноститься к вам:")
if g7==1:
	print("Жаждет вам смерти")
elif g7==2:
	print("Ненавидит вас")
elif g7==3:
	print("Завидует вам")
elif g7>=4 and g7<=7:
	print("Нечего особенного")
elif g7==8:
	print("Любит вас")
elif g7==9:
	print("Равняеться на вас")
elif g7==10:
	print("Ревнует вас")
else:
	print
#Основная черта
if g8>=1 and g8<=10:
    print("Черта характера:") 
if g8==1:
	print("Скромность")
elif g8==2:
	print("Агрессивность")
elif g8==3:
	print("Доброта")
elif g8==4:
	print("С причудами")
elif g8==5:
	print("Вдумчивость")
elif g8==6:
	print("Болтливость")
elif g8==7:
	print("Романтичность")
elif g8==8:
	print("Строгость")
elif g8==9:
	print("Уныние")
elif g8==10:
	print("Инфантильность")
else:
	print


input("")