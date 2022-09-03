from ast import Global


GLOBAL_VARIABLE = 10

def create_account(first_param, second_param, third_param=3, forth_param=4):
    """ ddd """
    print(first_param, second_param, third_param, forth_param)
    print(GLOBAL_VARIABLE)

    def inner_function():
        print(GLOBAL_VARIABLE)
    return first_param

create_account(1, 2, 3, 4)