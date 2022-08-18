your_name=input('Please write your name: ')
your_age=(int(input('How old are you? ')))+1
your_age=str(your_age)
template='Hello {your_name}, on your next birthday youll be {your_age} years'
print(template.format(your_name=your_name, your_age=your_age))