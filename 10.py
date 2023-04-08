# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит число N - количество
# элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива
# Ввод:              Вывод:
# 7                 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

def massiv_chisel():
    set_num = int(input('введите длину набора чисел: '))
    set = []
    for i in range(set_num):
        set.append(int(input(f'запишите {i+1} число в первый набор--> ')))
    return set

# l1 = massiv_chisel()
# l2 = massiv_chisel()

# new_list = []

# for item in l1:
#     if item not in l2:
#         new_list.append(item)

# print(new_list)

# def remove_el(lst1, set2):
#     for i in set2:
#         while i in lst1:
#             lst1.remove(i)
#     return(lst1)

# l1 = [int(input(f"Введите элемент массива {i + 1}: ")) for i in range(int(input("Введите длину массива: ")))]
# l2 = set([int(input(f"Введите элемент массива {i + 1}: ")) for i in range(int(input("Введите длину массива: ")))])

# print(l1)
# print(l2)
# print(*remove_el(l1, l2))


def poisk_bolsh_soseda(set, num):
    count = 0
    for i in range(len(set)-1):
        # print(set[i-1])
        if set[i] == num:
            if set[i-1] < set[i] > set[i+1]:
                count += 1
    return count


l1 = massiv_chisel()
num = int(input('введите число: '))

print(poisk_bolsh_soseda(l1, num))
