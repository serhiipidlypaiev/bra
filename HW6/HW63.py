list100 = list(range(1,101))
print(list100)
list5=[]
i=0
while i<=len(list100)-1:
    if ((list100[i])//7 and (list100[i])%5!=0):
        list5==list5.append(list100[i])
    i+=1
print(list5)



