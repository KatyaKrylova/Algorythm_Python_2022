n=int(input())#количество чисел в массиве
count=0
mas=list(map(int, (input().split())))#map позволяет применить функцию int для каждого итерируемого объекта
#(разделяем числа,введеные ранее по пробелу,например n = 1 2 3 4 получим ["1","2","3","4"])
for i in range(n-1):#от начала к концу от 0 до 3(индекс элемента), если n = 4
                for j in range(n-i-1):#от конца к началу от 3 до 0, если n = 4 
                    if mas[j] > mas[j+1]:
                        mas[j], mas[j+1] = mas[j+1], mas[j]
                        count+=1
                        print(" ".join(map(str, mas)))
if count==0:
    print(0)