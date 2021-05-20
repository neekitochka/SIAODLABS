import random
import numpy as np
import random
from queue import PriorityQueue

print("Hello World!")

m = input("Введите количесвто столбцов: ")
n = input("Введите количесвто строк: ")
m = int(m)
n = int(n)
if m == 0 and n == 0:
    m = 50
    n = 50
min_limit = -250
max_limit = 1012
# Создание матрицы
mas = np.zeros((m, n))
# Генерация мартицы 50 на 50
for i in range(m):
    for j in range(n):
        mas[i][j] = random.randint(int(min_limit), int(max_limit)) #Генерируем матрицу


def tourney_sort(array):
    sorted_array = []
    pq = PriorityQueue()
    for i, num in enumerate(array):
        pq.put(num)
    while not pq.empty():
        sorted_array.append(pq.get())
    return sorted_array


print(mas)
new_array5 = [[random.randint(min_limit, max_limit) for row in range(0,n)] for row in range(0,m)]
for i in range(m):
    print(tourney_sort(new_array5[i]))
print("\n")