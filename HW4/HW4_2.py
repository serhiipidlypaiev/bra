iii=3
summ=(int(input('Скільки будет 10+10: ')))
#mult=(int(input('Скільки будет 10*10: ')))1
while iii>0:
    if summ == 10+10:
        print('Вірно, 10+10 = 20')
        break
    else:
        summ=(int(input('Не правильно, залишилось ' + str(iii) + ' спроби Скільки будет 10+10,: ')))
        iii=iii-1
    print('Відповідь не правильна')
