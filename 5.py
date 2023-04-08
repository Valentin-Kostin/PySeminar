# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]

# Output: 6

n = [1, 1, 2, 0, -1, 3, 4, 4]

print(len(set(n)))

# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на
#  K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_n = [1, 2, 3, 4, 5]
k = 3
list_n = list_n[-k + 1:] + list_n[:-k + 1]
print(list_n)

# Напишите программу для печати всех уникальных значений в словаре.
dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
             {"VII": "S005"}, {" V ": "S009"}, {" VIII ": "S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

all_vals = set()
for into_dict in dict_list:
    val_set = set(into_dict.values())

    all_vals |= val_set

print(all_vals)

