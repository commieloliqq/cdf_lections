# 1)Дано: переменная digits = '123456789'
# Необходимо вывести сумму цифр, представленных в виде одного строкового значения '123456789'. Сумма этих цифр составляет 45. Напишите код, который выдаст эту её.
# Подсказка: используйте генератор списка, функцию int(), функцию sum() для суммирования списка, состоящего из чисел.
# digits = '123456789'
# print(sum(list(map(int, digits))))

# 2) напишите лямбда функцию
# которая принимает одно число, и возводит его в квадрат
# a = lambda x: x * x
# print(a(5))

# 3) напишите лямбда функцию которая принимает 2 числа, первое число возводите в степень второго числа
# a = lambda a,b: a**b
# print(a(5,3))

# 4) напишите лямбда функцию 
# которая принимает список имён, и функция должна приветствовать все имена (используйте функцию map)
# print(list((map(lambda x: f'{x} privet', ['Andew', 'Alishonktoni', 'Herobrine', 'Sanya']))))

# 5) напишите лямбда функцию 
# которая принимает список чисел, и она будет фильтровать этот список,
#  то есть будет принимать только те числа которые делятся на 5, использовать встроенные функции filter, list
# ls = [1,2,3,4,5,6,7,8,9, 10]
# print(list(filter(lambda x: x % 5 == 0, ls)))
a = input('123')
print(a)