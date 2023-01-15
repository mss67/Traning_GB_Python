#Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

hh = '00'
mm = '00'
sec = int(input('Введите время в секундах: '))

if sec < 60:
     if sec < 10:
        print(hh, ':', mm, ':', '0' + str(sec))
     else:
        print(hh, ':', mm, ':', sec)
elif 3600 > sec > 60:
    mm = sec // 60
    sec = sec % 60
    if mm < 10:
        print(hh, ':', '0' + str(mm), ':', sec)
    else:
        print(hh, ':', mm, ':', sec)
elif sec >= 3600:
    hh = sec // 3600
    sec = sec - (hh * 3600)
    if sec < 60:
         print(hh, ':', mm, ':', sec)
    elif 3600 >= sec > 60:
        mm = sec // 60
        sec = sec % 60
        if mm < 10:
            print(hh, ':', '0' + str(mm), ':', sec)
        else:
            print(hh, ':', mm, ':', sec)
    print(hh, ':', mm, ':', sec)
