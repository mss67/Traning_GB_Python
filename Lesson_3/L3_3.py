'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
arg1 = int(input('Число 1: '))
arg2 = int(input('Число 2: '))
arg3 = int(input('Число 3: '))

def my_func (arg1, arg2, arg3):
    sum = arg1 + arg2 + arg3 - min(arg1, arg2, arg3)
    print(sum)


my_func(arg1, arg2, arg3)
