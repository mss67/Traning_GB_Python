# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
# Для решения используйте цикл while и арифметические операции.

a = int(input('Введите целое положительное число: '))

m = a % 10
a = a // 10
while a > 0:
    print (a)
    if a % 10 > m:
        m = a % 10
    a = a // 10
print(m)

# я не понимал как сделать это задание, поэтому нашёл в интернете и попробовал разобраться с ним. 
# Вроде начал понимать что тут происходит