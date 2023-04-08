# Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам.

# i = int(input("Введите число: "))
# maxN = i
# while i != 0:
#     i = int(input("Введите число: "))
#     if i > maxN:
#         maxN = i
# print(maxN)

maxN = 0
while (i := int(input("Введите число: "))) != 0:
    if i > maxN:
        maxN = i
print(maxN)
