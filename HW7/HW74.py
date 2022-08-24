list1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dic1 = {}
b=1
for i in range(len(list1)):
    dic1.update({b:list1[i]})
    b+=1
inv_dic1 = {v: k for k, v in dic1.items()}
print(dic1)
print(inv_dic1)