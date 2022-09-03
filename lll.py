def persistence(n):
    if n < 10: return n

    multiplier = 1

    while(n > 0):
        multiplier = (n % 10) * multiplier
        n = n // 10
    return persistence(multiplier) + 1
print(persistence(15))

# def sum_digits(num, count = 1, num1 = 0):
#     if num > 9:
#         num1 = num%10 * sum_digits(num//10) if num > 9 else num
#     else:
#         return sum_digits(num1, count+1)
   
# print(sum_digits(num = 999))

    
#     if len(str(n)) == 1:
#         return 0
#     digit = 1
#     for i in str(n):
#         digit *= int(i)
#     n = test_funct(digit)
#     return test_funct(n)
    
#     # if index == 0:
#     #     return 0
#     # if index == 1:
#     #     return 1
#     # return test_funct(index - 2) + test_funct(index - 1)


# print(test_funct(15))

# def persistence(number):
#     if number < 10:
#         return 0

#     new_number = multiply_all(get_digits(number))
#     return 1 + persistence(new_number)