
# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

a = int(input("Введите чисоло a: "))
b = int(input("Введите чисоло b: "))

def sum (a,b):
    if b==0:
        return a
    return sum (a+1, b-1)


print(sum(a,b))