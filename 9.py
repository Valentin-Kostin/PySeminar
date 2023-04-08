# def num_sum(x, y):
#     coef = 1000
#     print(coef)
#     return x + y
# coef = 4

# print(num_sum(2, 6))
# print(coef)


# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def febonachi(k):
#     # print(k)
#     if k > 1:
#         a = febonachi(k-1)+febonachi(k-2)
#         # print(a)
#         return a
#     return 1
# k = int(input("Введите число: "))
# print(febonachi(k))


# Хакер Василий получил доступ к классному журналу и хочет
# заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1

# def massiv_chisel():
#     set_num = int(input('введите длину набора чисел: '))
#     set = []
#     for i in range(set_num):
#         set.append(int(input(f'запишите {i} число в первый набор--> ')))
#     return set


# def zamena_ocenok(set):
#     min_num = min(set)
#     max_num = max(set)
#     for i in range(len(set)):
#         if set[i] == max_num:
#             set[i] = min_num
#     # while max_num in set:
#     #     max_index = set.index(max_num)
#     #     set[max_index]=min_num
#     return set


# print(zamena_ocenok(massiv_chisel()))


# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы
# и использовать циклы (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def rev_str(n):
    el = input()
    if n == 1:
        return el
    return rev_str(n-1) + ' ' + el

def num_reverse(m):
    if m == 0:
        return
    x = input()
    num_reverse(m - 1)
    print(x, end=" ")

n =int(input())
print(rev_str(n))
num_reverse(n)