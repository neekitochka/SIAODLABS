from random import randint
from math import sqrt

# Создание списка, его сортировка по возрастанию и вывод на экран
arr = []
r = randint(3, 10)
for i in range(r):
    arr.append(randint(1, 100))  # append добавляет элемент в список
print(arr)
arr.sort()
print(arr)


def Triangle(arr):
    el1 = -1
    el2 = -2
    el3 = -3
    counter = 0
    while arr[el1] >= arr[el2] + arr[el3] or arr[el2] >= arr[el1] + arr[el3] or arr[el3] >= arr[el1] + arr[el2]:
        counter += 1
        if counter + 2 == len(arr):
            break
        elif counter % 3 == 1:
            el3 -= 1
        elif counter % 3 == 2:
            el2 -= 1
        elif counter % 3 == 0:
            el1 -= 1

    if counter + 2 != len(arr):
        print("Стороны треугольника с максимальным периметром:", arr[el3], arr[el2], arr[el1])
        p = arr[el3] + arr[el2] + arr[el1]
        print("Периметр =", p)
        pol = p / 2
        s = sqrt(pol * (pol - arr[el3]) * (pol - arr[el2]) * (pol - arr[el1]))
        if s <= 0:
            print("Площадь = 0")
        else:
            print("Площадь =", s)
    else:
        print("В данном массиве не существует треугольников!")


Triangle(arr)


