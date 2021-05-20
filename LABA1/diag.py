def sortDiag(mat):
    # Размер матрицы
    m, n = len(mat), len(mat[0])

    # Пустой массив для диагоналей исходной матрицы
    temp = [[] for i in range(m + n)]

    # Добавляем каждую диагональ в массив temp
    for i in range(m):
        for j in range(n):
            temp[i - j].append(mat[i][j])

    # Сортируем каждую диагональ (т.е линию) массива
    for line in temp:
        line.sort(reverse=True)

    # "Линии" в диагонали матрицы
    for i in range(m):
        for j in range(n):
            # pop() удаляет последний элемент массива и возвращает его
            mat[i][j] = temp[i - j].pop()
    return mat


arr = [[11, 57, 12, 10], [24, 27, 19, 21], [31, 15, 14, 21], [13, 52, 14, 21]]
print("mat:")
for l in arr:
    print(l)
print("\nSorted: ")
arr = sortDiag(arr)
for l in arr:
    print(l)
arr = [[81, 41, 75, 89, 11], [12, 86, 61, 55, 78], [71, 88, 99, 97, 51], [17, 33, 85, 79, 58],
       [45, 83, 59, 69, 19]]
print("\nmat:")
for l in arr:
    print(l)

print("\nSorted: ")
arr = sortDiag(arr)
for l in arr:
    print(l)