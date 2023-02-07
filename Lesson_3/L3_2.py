'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать 
параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''
fname = input('Имя: ')
sname = input('Фамилия: ')
birthday = input('День рождения: ')
sity = input('Город проживания: ')
email = input('email: ')
phone = input('ТелефонЖ ')

def contact(fname, sname, birthday, sity, email, phone):
    # full_contact = fname, sname, birthday, sity, email, phone
    print(fname, sname, birthday, sity, email, phone)
    
contact('Контакт: ', fname, sname, birthday, sity, email, phone)