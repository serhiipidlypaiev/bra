import random
i=10
n=10
list1=[]
list2=[]
list3=[]
while i>=0:
    i-=1
    number = random.randint(1,100)
    list1.append(number)
while n>=0:
    n-=1
    number1 = random.randint(1,100)
    if number1 in list1 and number not in list3:
        list3.append(number1)
    list2.append(number1)
print('Random list1: ', list1)
print('Random list12: ', list2)
print('Common integers: ', list3)