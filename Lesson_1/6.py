'''
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''

x = int(input('Сколько километров прошёл спортсмен в первый день: '))
y = int(input('Сколько километров должен пройти спортсмен: '))
day = 1
summ = 0
while x < y:
    summ = x * 0.1
#    day += 1
print(f'На {day} день спортсмен пробежал {summ} километров')


'''
Не понимаю как тут решить. Оставлю так.
'''