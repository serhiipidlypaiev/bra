dict1 = {}
def make_country(counrty,capital):
    dict1.update({counrty:capital})
    for key, value in dict1.items():
        print(key, ' : ', value)
    return

while True:
    work = input('Do you want work? y or n: ')
    if work == 'y':
        make_country(print('Please write the country: '), print('Please write the capital: '))
    else:
        break
