#  Объявляем функцию add_everything_up, которая принимает два аргумента: a и b.

def add_everything_up(a, b):

#  Блок try:если оба аргумента - одного типа (например, оба числа или обе строки), будет выполнено сложение,
#  и результат вернется из функции.
    try:
        return a + b
#  Блок except:если a и b разных типов (например, число и строка), произойдет ошибка TypeError,в этом случае
#  мы обрабатываем ошибку и возвращаем строку, которая создается путем конкатенации строковых представлений a и b.
    except TypeError:
        return str(a) + str(b)

#  Пытаемся сложить число со строкой, возникает TypeError.
print(add_everything_up(123.456, 'строка'))
#  Сложение строки и числа, также TypeError
print(add_everything_up('яблоко', 4215))
#  Сложение двух чисел, успешное, выводит сумму двух чисел.
print(add_everything_up(123.456, 7))
#  Сложение двух строк выводит сумму строк.
print(add_everything_up('Синий', 'автомобиль'))