num=int(input())
mas=list(map(int, (input().split())))
buyers=int(input())
buy=list(map(int, (input().split())))
sell=[0]*num
for i in range(num):
    mas[i]=[mas[i],i+1]
for i in range(buyers):
    sell[buy[i]-1]+=1
for i in mas:
    if i[0]<sell[i[1]-1]:
        print('yes')
    else:
        print('no')