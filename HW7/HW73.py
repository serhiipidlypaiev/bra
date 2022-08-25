import random

list1 = []

for i in range(1, 10):
    number = random.randint(1, 10)
    number1 = number * number
    new_turp = (number, number1)
    list1.append(new_turp)
print(list1)
