def make_operation(input_list, result=0, result1=1 ):
    i=1
    if '+' in input_list[0]:
        while i < (len(input_list)):
            result += int(input_list[i])
            i+=1
        print('Summa = %d'%result)
    elif "-" in input_list[0]:
        while i < (len(input_list)):
            result -= int(input_list[i])
            i+=1
        print('Minus = %d'%result )
    elif '*' in input_list[0]:
        while i < (len(input_list)):
            result1 *= int(input_list[i])
            i+=1
        print("Multiply = %d"%result1)
    return
make_operation(input_list = (input('Write your data: ')).split(', '))

            
