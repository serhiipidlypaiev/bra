phone_number = input('Please write phone number: ')
iii = 5
while iii!=0:
    if str.isdigit(phone_number) and len(phone_number) == 10:
        print('Phon number is corect: ' + phone_number)
        break
    else:
        phone_number = input('Please write phone number is incorrect ')
        iii=iii-1
