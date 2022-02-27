def Answ():
    num=int(input())#количество чисел в массиве
    mas=[]
    for i in range(num):
        mas.append(list(map(int,input().split())))#добавление чисел в массив
        mas.sort(key = lambda x: x[1], reverse=True) #сортируем по первому элементу массива
        #( взадаче нужно отсортировать пару чисел,где первое дожно идти по возрастанию(если вторые одинаковые),
        # а второе по убыванию,напрмер 345 67
        #                              344 66
        #                              700  5
        #                              800  5                            
                                                                                                                                
    for j in range(num-1):
        for i in range(0,num-j-1):
            if mas[i][1]==mas[i+1][1]  and mas[i][0]>=mas[i+1][0]: #если вторые равны и в первом элемент,который выше, больше нижнего 
                mas[i][0],mas[i+1][0]=mas[i+1][0],mas[i][0]#меняем местами
    for i in range(num):
        print(mas[i][0],mas[i][1])# просто вывод
Answ()#вызов функции