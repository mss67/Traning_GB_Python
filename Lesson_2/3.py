'''
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict
'''

m = int(input('Введите номер месяца от 1 до 12: '))

m_dict = {'Январь': 1, 'Февряль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6, 'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабель': 12}
vg_dict = {'зима': ['декабрь', 'январь', 'февраль'], 'весна': ['март', 'апрель', 'май'], 'лето': ['июнь', 'июль', 'август'], 'осень': ['сентярь', 'октябрь', 'ноябрь']}
for el in m_dict:  # Проверка элементана на наличие в словаре
    if m_dict[el] == m:    # Если есть совпадение
        print(f'Это месяц: {el}')
        for vg in vg_dict.items:
            vg == m_dict[el]
            print(vg)
