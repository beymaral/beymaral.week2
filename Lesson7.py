#Conditional Statements

# a = [1, 2, 3, ]
# s = 'String'
# a.reverse(a)
# s.lower()
#
# print(a)
# print(s) == failure
# print(s.lower())


# IF
# num1 = int(input('num 1: '))
# num2 = int(input('num 2: '))


# if num1>num2:
#     print("{} is bigger then {}".format(num1, num2))
# elif num2 > num1:
#     print(f'{num1} is lower then {num2}')
# else:
#     print(f"")

# Calculator

# num1 = int(input('num 1: '))
# operator = input('operator:')
# num2 = int(input('num 2: '))


# if operator == '+':
#     result = num1+num2
#     print('result is: {}'.format(result))
# elif operator == '-':
#     result = num1-num2
#     print('result is: {}'.format(result))
# elif operator == '*':
#     result = num1*num2
#     print('result is: {}'.format(result))
# elif operator == '/':
#     result = num1/num2
#     print('result is: {}'.format(result))
# else:
#     print('not supported')

# if operator == '+':
#     result = num1+num2
#     print(f'result is: {result}')
# elif operator == '-':
#     result = num1-num2
#     print(f'result is: {result}')
# elif operator == '*':
#     result = num1*num2
#     print(f'result is: {result}')
# elif operator == '/':
#     result = num1/num2
#     print(f'result is: {result}')
# else:
#     print('not supported')


# lists = [1, 3, 4, 5, ]
# if 2 in lists:
#     print("1")


# OR AND
# lists = [12, 22, 18, 19, 24, 16, 7, ]
# if 22 in lists and (25 in lists):
#     print('We support this ages')
# else:
#     print('We do not support this ages')

# lists = [12, 22, 18, 19, 24, 16, 7, ]
# a = int(input())
# b = int(input())
# if a in lists or b in lists:
#     print('We support this ages')
# else:
#     print('We do not support this ages')

# Tasks

# lists_1 = list(range(1, 1000))
# lists_2 = []
# for i in lists_1:
#    if (i%2)==0 and (i%7)==0 and (i%15)==0:
#         lists_2.append(i)
# print(lists_2)

#2
# system = input('Please tell us the metric system C or F:')
# degree = float(input('Please type the degree you want to convert:'))
#
# if system.lower() == 'c':
#     if degree < -273.5:
#         print("We do not support")
#     elif degree == -273.5:
#         print("It is absolute Zero 0")
#     else:
#         print((degree*9/5)+32)
#
# elif system.lower() == 'f':
#     print((degree - 32) * 5 / 9)


# years = int(input())


# if (years % 4) == 0:
#     if(years % 100) != 0:
#         print('No')
#         if(years % 400) == 0:
#             print('Yes')
#     print('Yes')
# else:
#     print('No')
#???
# a = int(input('pls enter a number :'))
# for i in range(0, 11):
#     print(f'(a+i), '* 2 =', (i+1)*2)
# a = int(input('pls enter a number :'))
# for i in range(1, 11):
#     print(f'{a} * {i} = {a * i}')

for i in range(1, 6):
    print('Ulan'*i)









