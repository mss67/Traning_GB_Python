'''
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
'''

vyr = float(input('Введите выручку организации: '))
izd = float(input('Введите убыток организации: '))
prib = 0
if vyr < 0 or izd <= 0:
    print("Выручка не должна быть меньше 0. Издержки должны превышать нулевое значние!")
else:
    if vyr >= izd and vyr != 0 and izd !=0:
        prib = vyr - izd
        print(F'Вы в прибыли: {prib}')
        print(f'Рентабельнрость: {prib / vyr} рублей')
        sotr = int(input('сколько сотрудников в фирме? - '))
        if sotr != 0:
            print(f'Прибыль на сотрудника составила: {vyr / sotr} рублей')
        else:
            print('Колличество сотрудников не дожно быть равным 0')
    else:
        print(f'В убытке на: {izd - vyr} рублей')
