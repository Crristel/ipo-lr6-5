import random #подключаем модуль random
spisok=[random.randint(-50,50) for i in range(1,25+1)] #с помощью генератора списка создаём список с числами в диапазоне от -50 до 50
print(spisok) #вывод нашего списка
print() #для перехода на новую строку 
poloznum=0 # счётчик для положительных чисел 
otriznum=0 #счётчик для отрицателььных чисел 
nyl=0 #счётик для нулей
list1=[] #создание списка, в который будут записаны положительные числа 
list2=[] #создание списка, в который будут записаны отрицательные числа 
list3=[] #создание списка, в который будут записаны нули 
for i in spisok: # цикл для нахождения полжительных, отрицательных чисел и нулей 
    if i>0: #если число больше нуля 
        poloznum+=1 #к переменной poloznum добавляем 1
        list1.append(i) #добавляем переменную в список, который будет состоять из положительных чисел 

    elif i<0: #если число меньше нуля 
        otriznum+=1 #к переменной otriznum добавляем 1
        list2.append(i) #добавляем переменную в список, который будет состоять из отрицательных чисел 
    elif i==0: #если число равно нулю
        nyl+=1# к переменной nyl добавляем 1
        list3.append(i) #добавляем переменную в список, который будет состоять из нулей
print("Положительные числа:",list1) #вывод на консоль
print("Количество положительных чисел в списке:",poloznum)#вывод на консоль
prosent1=poloznum/25*100 #находим процент положительных чисел от общего кол-ва
print("Процент положительных чисел от общего количества чисел",prosent1)#вывод на консоль
print()#для перехода на новую строку 
print("Отрицательные числа:",list2)#вывод на консоль
print("Количество отрицательных чисел в списке:",otriznum)#вывод на консоль
prosent2=otriznum/25*100 #находим процент отрицательных чисел от общего кол-ва
print("Процент отрицательных чисел от общего количества чисел",prosent2)#вывод на консоль
print()#для перехода на новую строку 
print("Нули:",list3)#вывод на консоль
print("Количество нулевых чисел в списке:",nyl)#вывод на консоль
prosent3=nyl/25*100 #находим процент нулей от общего кол-ва
print("Процент нулевых чисел от общего количества чисел",prosent3)#вывод на консоль
print()#для перехода на новую строку 
max=max(spisok) #находим максимальное число в списке с помощью функции max()
print("Максимальное число в списке:",max)#вывод на консоль
print()#для перехода на новую строку 
min=min(spisok) #находим  минимиальное число в списке с помощью функции min()
print("Минимальное число в списке:",min)#вывод на консоль