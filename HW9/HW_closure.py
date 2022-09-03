# print('Please write number: ')


def outside_func():
    firtst_number = int(input("Please write number: "))

    def inside_func(number):
        if number >= 100:
            return print("Number >= 100 ")
        if number < 100:
            return print("Number < 100 ")

    return inside_func(firtst_number)


outside_func()
