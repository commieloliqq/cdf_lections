"""
1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
"""
# def sum1(a: int = 0, b: int = 0) -> int:
#     '''Возвращает сумму аргументов "a" и "b" '''
#     return a + b

# print(sum1(1,2))
"""
2) Создайте функцию, которая будет принимать строку. Функция должна выводить длину этой строки(не использовать функцию len).
"""
# def len1(str):
#     l = 0
#     for _ in str:
#         l += 1
#     return l
# print(len1('12345'))
"""
3) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
"""
# def type_ab(a, b):
#     return type(a), type(b)
# print(type_ab('1', 2))
"""
4) Создайте функцию, которая должна принимать 2 числа и возвращать результат их деления.
"""
# def div1(a, b):
#     return a / b
# print(div1(2,1))
"""
5) Создайте функцию, которая принимает словарь. Пройдитесь по словарю циклом и распечатайте все его ключи
"""
# def func1(a: dict):
#     for k in a.keys():
#         print(k)
# func1({'123': 123, '456': 456, '789k': 789})
"""
6) Создайте функцию, которая принимает и выводит "It's odd number" если это число не кратно двум и "It's even number" в противном случае.
"""
# def odd_even1(a):
#     print("It's odd number" if a % 2 != 0 else "It's even number")
# odd_even1(4)
"""
7) Напишите функцию, которая будет принимать строку и проверять является ли она палиндромом. Пробелы и регистр учитывать не нужно.
(Палиндро́м, пе́ревертень — число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например, число 101; слова "кок", "топот", "комок" и т.д.)
"""
# def isPalindrom1(str):
#     return True if str == ''.join(reversed(str)) else False
# print(isPalindrom1('11'))
"""
8) Создайте функцию которая принимает от пользователя два числа. Она должна сравнить эти числа между собой и вывести максимальное значение.
"""
# def max1(a, b):
#     c = [a, b]
#     print('max:', max(c), f'\n{a} > {b}' if a > b else f'\n{a} > {b}')
# max1(4, 3)
"""
9) Напишите функцию, которая принимает список чисел и возвращает их произведение.
"""
# def mul_ls1(a: list):
#     r = 1
#     for i in a:
#         r = r * i
#     return r
# print(mul_ls1([1, 2, 4]))
"""
10) Напишите функцию, которая принимает целое число и возвращает сумму всех его цифр. Например, число 123 --> 6
"""
# def digit_sum1(a: int):
#     a = str(a)
#     b = 0
#     for i in a:
#         b += int(i)
#     return b
# print(digit_sum1(111))