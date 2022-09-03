getstring = input('Write the string: ')
if len(getstring) >=2:
    first_chars = getstring[:2]
    last_chars = getstring[-2:]
    print('First and last chars are: '+ first_chars + last_chars)
else:
    print('Empty String')
