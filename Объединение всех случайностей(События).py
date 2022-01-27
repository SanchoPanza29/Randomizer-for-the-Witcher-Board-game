import random

input("Нажмите Enter выпадет случайное Важное событие (Удача и неудача,Союзники и враги,Любовь:)")

print("")
bc=random.randint (1,37)
bc12=random.randint (1,10)
bc13=random.randint (100,1000)
bc14=random.randint (1,12)
bc15=random.randint (700,710)
bc16=random.randint (1,10)
bc17=random.randint (1,4)


if bc>=15 and bc<=21:
	print("Неудача:")
	if bc12==1:
		print("Долг")
		print(str(bc13)+ " Крон")
	elif bc12==2:
		print("Заключение "+str(bc14)+" месяцев")
	elif bc12==3:
		print("Любимый,друг или родственик убит")
	elif bc12==4:
		print("Ложное обвинение")
	elif bc12==5:
		print("В розыске")
	elif bc12==6:
		print("Предательсво :")
	elif bc12==7:
		print("Несчастный случай")
	elif bc12==8:
		print("Физическая или психическая травма")
	elif bc12==9:
		print("Проклятие")
	elif bc12==10:
		print("Зависимость:")
	else:
		bc12==11
#Любимый,друг или родственик убит
	if bc>=15 and bc<=21 and bc12==3:
		print("Что произошло:")
	if bc16>=1 and bc16<=5 and bc12==3 :
		print("Это был несчастный случай")
	elif bc16>=6 and bc16<=8 and bc12==3:
		print("Убит чудовищем")
	elif bc16==9 and bc12==3:
		print("Убит разбойниками")
	elif bc16==10 and bc12==3:
		print("Убит человеком")
	else: bc16==11
#Ложное обвинение
	if bc>=15 and bc<=21 and bc12==4:
		print("Вас обвинили: ")
	if bc16>=1 and bc16<=3 and bc12==4:
		print("В воровстве")
	elif bc16==4 and bc16==5 and bc12==4:
		print("В трусости или предательстве")
	elif bc16>=6 and bc16<=8 and bc12==4:
		print("В убийстве")
	elif bc16==9 and bc12==4:
		print("В изнасилование")
	elif bc16==10 and bc12==4:
		print("В нелегальном колдовстве")
	else: bc16==11
#В розыске
	if bc>=15 and bc<=21 and bc12==5:
		print("Вас разыскивают: ")
	if bc16>=1 and bc16<=3 and bc12==5:
		print("Несколько стражников ")
	elif bc16>=4 and bc16<=6 and bc12==5:
		print("В поселке ")
	elif bc16>=7 and bc16<=8 and bc12==5:
		print("В городе ")
	elif bc16==9 or bc16==10 and bc12==5:
		print("Во всем королевстве")
	else: bc16==11
#Предательсво
	if bc>=15 and bc<=21 and bc12==6:
		print
	if bc16>=1 and bc16<=3 and bc12==6:
		print("Вас шантажируют ")
	elif bc16>=4 and bc16<=7 and bc12==6:
		print("Ваша тайна раскрыта ")
	elif bc16>=8 and bc16<=10 and bc12==6:
		print("Вас предал кто-то из близких")
	else: bc16==11
#Несчастный случай
	if bc>=15 and bc<=21 and bc12==7:
		print("Что произошло:")
	if bc16>=1 and bc16<=4 and bc12==7:
		print("Вы изуродованы")
	elif bc16>=5 and bc16<=6 and bc12==7:
		print("Вы личились " +str(bc14)+" месяцев ")
	elif bc16>=7 and bc16<=8 and bc12==7:
		print("Вы потеряли память о " +str(bc14)+" месяцех того года")
	elif bc16>=9 and bc16<=10 and bc12==7:
		print("Вас мучают жуткие кошмары(с вероятностью 70% каждый раз во время сна)")
	else: bc16==11
#Физ и психическая травма
	if bc>=15 and bc<=21 and bc12==8:
		print("Что произошло:")
	if bc16>=1 and bc16<=3 and bc12==8:
		print("Вас отравили")
	elif bc16>=4 and bc16<=7 and bc12==8:
		print("Вы страдаете от панически атак")
	elif bc16>=8 and bc16<=10 and bc12==8:
		print("У вас серьезное душевное расстройство,вы агрессивны, иррациональны и депрессивны, а также слышите голоса.")
	elif bc16>=9 and bc16<=10 and bc12==8:
		print("Вас мучают жуткие кошмары(с вероятностью 70% каждый раз во время сна)")
	else: bc16==11
#Проклятие 
	if bc>=15 and bc<=21 and bc12==9:
		print("Название порчи:")
	if bc16>=1 and bc16<=2 and bc12==9:
		print("Теневая порча")
	elif bc16>=3 and bc16<=4 and bc12==9:
		print("Вечный зуд ")
	elif bc16>=5 and bc16<=6 and bc12==9:
		print("Дьявольская удача")
	elif bc16>=7 and bc16<=8 and bc12==9:
		print("Кошмар")
	elif bc16==9 and bc12==9:
		print("Поцелуй Песты")
	elif bc16==10 and bc12==9:
		print("Звериная порча")
	else: bc16==11
#Зависимость 
	if bc>=15 and bc<=21 and bc12==10:
		print
	if bc16>=1 and bc16<=5 and bc12==10:
		print("Пиво")
	elif bc16>=6 and bc16<=10 and bc12==10:
		print("Фиштех")
	else: bc16==11
	



if bc>=22 and bc<=28:
	print("Удача:")
	if bc12==1:
		print("Джекпот")
		print("Вы выйграли "+str(bc13)+" Крон")
	elif bc12==2:
		print("Учитель")
	elif bc12==3:
		print("Благодарность дворянина")
	elif bc12==4:
		print("Боевой инструктор")
	elif bc12==5:
		print("Благодарность Ведьмка")
	elif bc12==6:
		print("Дружба с разбойниками")
	elif bc12==7:
		print("Прирученый зверь")
	elif bc12==8:
		print("Благодарность мага")
	elif bc12==9:
		print("Благословение жреца")
	elif bc12==10:
		print("Рыцарство")
	else:
		bc12==11

bc1=random.randint (1,2) #2й  рандом четное\нечетное
bc2=random.randint (1,10)#3й рандом что или кто (отрицательное)
bc22=random.randint (1,10) #положительное
bc3=random.randint (1,10) # Уточнение
bc4=random.randint (1,10) # Уточнение как познакомились  или причины вражды
bc5=random.randint (1,10) # Уточнение на сколько знакомы или потерпевшая сторона
bc6=random.randint (1,10) # Уточнение Где находиться союзник или на сколько силен
bc7=random.randint (1,10) # Уточнение Где находиться союзник Насколько далеко все зашло?
bc8=random.randint (1,10) # В чем сила врага ?



#Союзники
if bc>=1 and bc<=7:
	print("Союзник")   
	if bc2>=1 and bc2<=5:
		print("Мужчина")
	if bc2>=6 and bc2<=10:
		print("Женщина")
	else :
		bc3==11
	if bc3==1:
		print("Охотник за головами")
	elif bc3==2:
		print("Маг")
	elif bc3==3:
		print("Наставник или учитель")
	elif bc3==4:
		print("Друг детства")
	elif bc3==5:
		print("Ремесленник")
	elif bc3==6:
		print("Бывший враг")
	elif bc3==7:
		print("Князь/Княгиня")
	elif bc3==8:
		print("Жрец/Жрица")
	elif bc3==9:
		print("Воин")
	elif bc3==10:
		print("Бард")
	else:
		bc3==11

	if bc>=1 and bc<=7: #Как познакомились
		print("Как вы познакомились:")
	if bc4==1:
		print("Вы его/ее спасли")
	elif bc4==2:
		print("Встретились в таверне")
	elif bc4==3:
		print("Он/она спас/спасла вас")
	elif bc4==4:
		print("Он/Она напал/напала на вас")
	elif bc4==5:
		print("Вы вместе попали в ловушку")
	elif bc4==6:
		print("Вам пришлось работать вместе")
	elif bc4==7:
		print("Вы его/ее нашли")
	elif bc4==8:
		print("Свелись по пьяни")
	elif bc4==9:
		print("Встетились в дороге")
	elif bc4==10:
		print("Сражались вместе")
	else:bc4==11
# Насколько вы близки?
	if bc>=1 and bc<=7:
		print("На сколько вы близки: ")
	if bc5>=1 and bc5<=4:
		print("Знакомые")
	elif bc5>= 5 and bc5<=6:
		print("Друзья")
	elif bc5>= 7 and bc5<=8:
		print("Близкие друзья")
	elif bc5==9:
		print("Не разлей вода")
	elif bc5==10:
		print("Свзяны взаимной клятвой")
	else:bc5==11
# Где союзник
	if bc>=1 and bc<=7:
		print("Где находиться Союзник:")
	if bc6>=1 and bc6<=3:
		print("Королевства Севера")
	elif bc6>=4 and bc6<=6:
		print("Империя Нильфгаард")
	elif bc6>=7 and bc6<=9:
		print("Земли Старших Народов")
	elif bc6==10:
		print("За пределами")
	else:bc6==11


# Враги
if bc>=8 and bc<=14:
	print("Враг")
	if bc2>=1 and bc2<=5:
		print("Мужчина")
	if bc2>=6 and bc2<=10:
		print("Женщина")
	else :
		bc3==11
	if bc3==1:
		print("Бывший друг")
	elif bc3==2:
		print("Бывший возлюбленный/возлюбленная")
	elif bc3==3:
		print("Родственник")
	elif bc3==4:
		print("Враг детства")
	elif bc3==5:
		print("Культист")
	elif bc3==6:
		print("Бард")
	elif bc3==7:
		print("Воин")
	elif bc3==8:
		print("Разбойник")
	elif bc3==9:
		print("Князь/Княгиня")
	elif bc3==10:
		print("Маг")
	else:
		bc3==11

if bc>=8 and bc<=14: #Причины вражды 
	print("Причина вражды:")
	if bc4==1:
		print("Нападение")
	elif bc4==2:
		print("Потеря возлюбенного")
	elif bc4==3:
		print("Серьезное унижение")
	elif bc4==4:
		print("Проклятие")
	elif bc4==5:
		print("Обвинение в нелегальном колдовстве")
	elif bc4==6:
		print("Отказ в романтических притязаниях")
	elif bc4==7:
		print("Нанесение серьезной раны")
	elif bc4==8:
		print("Шантаж")
	elif bc4==9:
		print("Сорваные планы")
	elif bc4==10:
		print("Провокация нападения чудовищ")
	else:bc4==11
#Кто потерпевшая сторона:
	if bc>=8 and bc<=14:
		print("Кто потерпевшая сторона:")
	if bc5>=1 and bc5<=5:
		print("Ваш персонаж" )
	elif bc5>=6 and bc5<=10:
		print("Враг")
	else:bc5==11
#На сколько силен враг 
	if bc>=8 and bc<=14:
		print("На сколько силен враг:")
	if bc6==1 or bc6==2:
		print("Не опасен")
	elif bc6>=3 and bc6<=5:
		print ("Достаточно опасен ")
	elif bc6>=6 and bc6<=8:
		print ("Очень опасен")
	elif bc6==9:
		print ("Предельно опасен")
	elif bc6==10:
		print("Смертельно опасен")
	else: bc6==11
#Насколько далеко все зашло?
	if bc>=8 and bc<=14:
		print("Насколько далеко все зашло:")
	if bc7>=1 and bc7<=2:
		print("Вражда почти забыта")
	elif bc7>=3 and bc7<=4:
		print ("Есть желание ударить в спину")
	elif bc7>=5 and bc7<=6:
		print ("Нападение при встрече")
	elif bc7==7 or bc7==8:
		print ("Выслеживание ради мести")
	elif bc7==9 or bc7==10:
		print("Жажда крови")
	else: bc7==11
	# В чем сила врага
	if bc>=8 and bc<=14:
		print("В чем сила врага:")
	if bc8>=1 and bc8<=2:
		print("Социальная сфера")
	elif bc8>=3 and bc8<=4:
		print ("Знания")
	elif bc8>=5 and bc8<=6:
		print ("Физическая сила")
	elif bc8==7 or bc8==8:
		print ("Подручные")
	elif bc8==9 or bc8==10:
		print("Магия")
	else: bc8==11



if bc==28:
	print("Счастливая любовь")
elif bc>=29 and bc<=31:
	print( "Романтическая трагедия ")
elif bc>=32 and bc<=33:
	print("Трудная любовь")
elif  bc>=34 and bc<=37:
	print("Шлюхи и разгул:")
else :
	print 
if bc>=29 and bc<=31 and bc2==1:
	print("Возлюбленный в плену")
elif bc>=29 and bc<=31 and bc2==2:
	print("Возлюбленный исчез")
elif bc>=29 and bc<=31 and bc2==3:
	print("Возлюбленный в тюрьме за преступления")
elif bc>=29 and bc<=31 and bc2==4:
	print("Возлюбленный жерта могущетвенного проклятия")
elif bc>=29 and bc<=31 and bc2==5:
	print("Возлюбленный бы убит вами")
elif bc>=29 and bc<=31 and bc2==6:
	print("Возлюбленный совершил самоубийство")
elif bc>=29 and bc<=31 and bc2==7:
	print("Возлюбленный в плену у дворяннина для гарема")
elif bc>=29 and bc<=31 and bc2==8:
	print("Возлюбленный был отбит сверстником")
elif bc>=29 and bc<=31 and bc2==9:
	print("Возлюбленный был убит чюдовищем")
elif bc>=29 and bc<=31 and bc2==10:
	print("Возлюбленный маг,разумное чудовище или ведьмак")
else :
	print

if bc>=32 and bc<=33 and bc2==1:
	print("Семья или друзья возлюбленного ненавидят вас")
elif bc>=32 and bc<=33 and bc2==2:
	print("Возлюбленный торгует своим телом")
elif bc>=32 and bc<=33 and bc2==3:
	print("Возлюбленный страдает от малой порчи или кошмаров")
elif bc>=32 and bc<=33 and bc2==4:
	print("Возлюбленный спит с кем попало")
elif bc>=32 and bc<=33 and bc2==5:
	print("Возлюбленный ужасно ревнив")
elif bc>=32 and bc<=33 and bc2==6:
	print("Вы с возлюбленным часто ругаетесь")
elif bc>=32 and bc<=33 and bc2==7:
	print("Вы и возлюбленный конкуренты в професии")
elif bc>=32 and bc<=33 and bc2==8:
	print("Возлюбленный другой расы")
elif bc>=32 and bc<=33 and bc2==9:
	print("Возлюбленный связан узами брака")
elif bc>=32 and bc<=33 and bc2==10:
	print("Ваши друзья или семья ненавидят вашего возлюбленного")
else:
	print


if bc>=34 and bc<=37 and bc2>=1 and bc2<=6:
	print("Вы наплодили "+str(bc17)+ " бастардов. Знают они вас или нет, решать вам")
elif bc>=34 and bc<=37 and bc2>=5 and bc2<=8:
	print("В одном из борделей, про вас пошли слухи")
elif bc>=34 and bc<=37 and bc2>=9 and bc2<=10:
	print("Подхватили болячку")
else:
	print

input('')