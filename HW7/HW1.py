data = input('Input your words: ')
list1 = data.split()
full={}
for key in list1:
    full[key] = full.get(key, 0) + 1
print('Dictionary: ', full)