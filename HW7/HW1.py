data = input('Input your words: ')
list1 = data.split(' ')
print(len(list1))
full={}
for n in list1:
    i=0
    k=0
    while i in range(len(list1)):
        if n == list1[i]:
            k+=1
        i+=1
    full.update({n:k})
print('Dictionary: ', full)