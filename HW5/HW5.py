import random
computer = random.randint(1,10)
person_number = input('Please write your number from 1 to 10: ')
if person_number==computer:
    print('You are win!')
else:
    print('You are lost!')
