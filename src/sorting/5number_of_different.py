num=int(input())
mas=list(map(int, (input().split())))#создали одномерный массив из введенных чисел [1,1,3]
slovar = dict(zip(mas,mas))#zip  для создания словаря из двух массивов [1:1,1:1,3:3]
print(len(slovar))#словарь работает так,что уберет одинаковые элементы 