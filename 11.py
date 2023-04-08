# Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n)
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k,
# не превосходящее 10'5. Программа должна вывести все пары дружественных чисел,
# каждое из которых не превосходит k. Пары необходимо выводить по одной в строке,
# разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284
import datetime




def sum_del(num):
    num_result = 0
    for i in range(1, num):
        if num % (i) == 0:
            num_result += i
    return num_result


def sech_paru(num):
    for i in range(num):
        n1 = sum_del(i)
        n2 = sum_del(n1)
        # print(i, n1, end='=')
        # print(n2)
        if i == n2 and n1 != n2 and n1 < n2:
            print(n1, n2)
            print(datetime.datetime.now()-a)


num = int(input('введите число: '))
a = datetime.datetime.now()
sech_paru(num)
print(datetime.datetime.now()-a)