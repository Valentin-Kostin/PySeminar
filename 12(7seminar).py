# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы
# используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
#  а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Svyatoslav Milovidov:


values = [1, 23, 42, 'asdfg']
transformed_values = list(map(lambda item: item, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')

print(values)
print(transformed_values)

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

old_list = [12, 6, 8, 18]
#           что сделать        где взять      при каком условии
new_list = [(item / 6 ) for item in old_list if item % 6 == 0]
print(old_list)
print(new_list)

def find_farthest_orbit(orb):
    pl_orb = [(a*b) for (a, b) in orb if a!=b]
    i = pl_orb.index(max(pl_orb))
    return orb[i]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(orbits)
print(find_farthest_orbit(orbits))

def find_farthest_orbit(orb):
    return max([(a*b, (a,b)) for (a, b) in orb if a!=b])

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(orbits)
print(find_farthest_orbit(orbits)[1])

# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

def same_by(func, vals):
    return len(set(map(func, vals))) <= 1 

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

# тернарный оператор
a = [1, 2, 6, 5]

list_=[(item+10 if item > 3 else item - 10) for item in a if not item%2]
print(list_)

# генератор словарей
from math import pi
def find_farthest_orbit(orbit):
    return max({pi * a * b: (a, b) for a, b in orbit if a != b}.items() )

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(find_farthest_orbit(orbits)[1])