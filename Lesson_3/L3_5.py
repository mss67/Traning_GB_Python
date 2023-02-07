"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""
my_list = list(input('текст: '))

def int_func(my_list):
    text = my_list()
    text[0] = text[0].upper()
    return ''.join(text)

int_func(my_list)

# Ну в общем не знаю как правильно
