'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

out_f = open("L5_1.txt", "w+", encoding="utf-8")
str_file = input("Введите строку: ")
while str_file:
    out_f.writelines(str_file)
    str_file = input("Введите строку: ")
    if not str_file:
        break

out_f.close()

with open("L5_1.txt") as new_f:
    for line in new_f:
        print(line)