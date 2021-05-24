"Задание №1. Треугольник с максимальным периметром"
print("\nЗадание №1.\n")
from random import randint
from math import sqrt


arr = []
r = randint(3, 10)
for i in range(r):
    arr.append(randint(1, 100))
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



"Задача №2. Максимальное число"
print("\nЗадание №2.\n")
def maxNumber(L):
    maxLength = len(str(max(L)))
    L = map(str, L)

    def sortKey(s):
        return s + s[-1] * (maxLength - len(s))

    sortedList = sorted(L, key=sortKey, reverse=True)
    return ''.join(sortedList)

print(maxNumber([15, 71, 17, 56, 22, 96]))

"Задача №3. Сортировка диагоналей в матрице"
print("\nЗадание №3.\n")
def sortDiag(mat):
    # Размер матрицы
    m, n = len(mat), len(mat[0])


    temp = [[] for i in range(m + n)]


    for i in range(m):
        for j in range(n):
            temp[i - j].append(mat[i][j])


    for line in temp:
        line.sort(reverse=True)


    for i in range(m):
        for j in range(n):

            mat[i][j] = temp[i - j].pop()
    return mat


arr = [[81, 41, 75, 89, 11], [12, 86, 61, 55, 78], [71, 88, 99, 97, 51], [17, 33, 85, 79, 58],
       [45, 83, 59, 69, 19]]
print("mat:")
for l in arr:
    print(l)

print("\nSorted: ")
arr = sortDiag(arr)
for l in arr:
    print(l)

"Задача №4. Шарики и стрелы"
print("\nЗадание №4.\n")


class balls:
    def __init__(self, mass):
        self.mass = mass
        self.count = 1

    def solution(self):
        if len(self.mass) == 0:
            self.count = 0
        else:
            m = 0
            for i in range(len(self.mass)):
                self.mass.sort()
            print(self.mass)
            for i in range(len(self.mass) - 1):
                if self.mass[m][1] < self.mass[i + 1][0]:
                    self.count = self.count + 1
                    m = i + 1
                elif self.mass[m][0] <= self.mass[i + 1][0] and self.mass[m][1] >= self.mass[i + 1][
                    1]:
                    m = i + 1

        return self.count


arr = [[2, 3], [2, 4], [6, 7], [7, 8]]
a = balls(arr)
print(a.solution())

"Задача №5. Стопки монет"
print("\nЗадание №5.\n")
def golds(piles):
    arr.sort()
    a = len(piles)//3
    ya = 0
    while a < len(piles):
        ya = ya + piles[a]
        a = a + 2
    return (ya)
print(golds([5,4,1,11,3,9,10,4,11]))

"Задача №6."
print("\nЗадание №6.\n")


def battle(str1, str2):
    sorted1 = ''.join(sorted(str1));
    sorted2 = ''.join(sorted(str2));
    firstWin = True;
    secondWin = True;

    for i in range(0, len(sorted1)):
        if not (sorted1[i] >= sorted2[i]):
            firstWin = False
            break;

    if not firstWin:
        for i in range(0, len(sorted1)):
            if not (sorted2[i] >= sorted1[i]):
                secondWin = False
                break;
    else:
        secondWin = False

    return (firstWin or secondWin)


print(battle('nik', 'ita'))
print(battle('saiod', 'privet'))

"Задача №7."
print("\nЗадание №7.\n")
s = "Nikita privet"
Output = ""
for i in range(len(s)):
    for j in range(0, i):
        sub = s[j:i + 1]
        if sub == sub[::-1]:
            if len(sub) > len(Output):
                Output = sub
print(Output)

"Задача №8."
print("\nЗадание №8.\n")
def conca(s):
    result = set()
    for l in range(1, len(s)//2+1):
        count = sum(s[i] == s[i+l] for i in range(l))
        for i in range(len(s)-2*l):
            if count == l:
                result.add(s[i:i+l])
            count += (s[i+l] == s[i+l+l]) - (s[i] == s[i+l])
        if count == l:
            result.add(s[len(s)-2*l:len(s)-2*l+l])
    return len(result)

print(conca("aabbaabb"))