import random
i=10
list=[]
while i>=0:
    number = random.randint(1,100)
    i-=1
    list.append(number)
print('List of number: ', list)
print('Max element in list', max(list))