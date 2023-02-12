arg1 = int(input('output_in_hours: '))
arg2 = int(input('bid_in_hour: '))
arg3 = int(input('prize: '))


def my_func(arg1, arg2, arg3):
    sum = arg1 * arg2 + arg3
    print(sum)


my_func(arg1, arg2, arg3)



# print("Имя скрипта: ", script_name)
# print("Выработка в часах: ", output_in_hours)
# print("Ставка в час: ", bid_in_hour)
# print("Премия: ", prize)
# print("Зарплата сотрудника: ", (float(output_in_hours) * float(bid_in_hour)) + float(prize))