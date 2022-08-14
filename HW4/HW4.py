getstring = input('Write the string: ')
if len(getstring) >=2:
    first_chars = getstring[:2]
    last_chars = getstring[-2:]
    print('First and last chars are: '+ first_chars + last_chars)
else:
    print('Empty String')


phone_number = input('Please write phone number: ')
    if str.isdigit(phone_number) and len(phone_number) == 10: