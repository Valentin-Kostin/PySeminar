number = int(input("Введите число: "))
f1 = f2 = 1
n = 3
while number>f2:
    f1, f2 = f2, f1 + f2
    n+=1
    print(f2, end=' ')
print(n if number == f2 else '-1')