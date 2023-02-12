from sys import argv

script_name, output_in_hours, bid_in_hour, prize, zarp = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", output_in_hours)
print("Ставка в час: ", bid_in_hour)
print("Премия: ", prize)
print(
    "Зарплата сотрудника: float(input('output_in_hours: ')) * float(input('bid_in_hour: ')) + float(input('prize: ')): ", zarp)

# python.exe L4-1.py output_in_hours, bid_in_hour, prize, zarp

# print("-------------------")
# arg1 = float(input('Выработка в часах:'))
# arg2 = float(input('Ставка в час:'))
# arg3 = float(input('Премия:'))
# arg4 = arg1 * arg2 + arg3

# argv = ['L4-2.py', arg1, arg2, arg3, arg4]

# scipt_name, output_in_hours, bid_in_hour, prize, zarp = argv

# print(scipt_name, output_in_hours, bid_in_hour, prize, zarp)
# print("-------------------")