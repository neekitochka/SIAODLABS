from random import randint

print("\nБинарный поиск\n")


arr = []
for i in range(15):
    arr.append(randint(1, 50))
arr.sort()
print(arr)


value = int(input("искать "))

value_delete = int(input("удалить "))

value_add = int(input("добавить "))

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = "not found"
    while (first <= last) and (index == "not found"):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid + 1
    return index


def BinarySearchDelete(arr, val_d):
    arr.pop(BinarySearch(arr, val_d))

def BinarySearchAdd(arr, val_a):
    arr.append(val_a)
    arr.sort()

print("ячейка", BinarySearch(arr, value))

BinarySearchDelete(arr, value_delete)
print("новый массив", arr)

BinarySearchAdd(arr, value_add)
print("новый массив", arr)



print("\nБинарное дерево\n")


arr = []
for i in range(15):
    arr.append(randint(1, 50))
print(arr)


value = int(input("искать "))

value_delete = int(input("удалить "))

value_add = int(input("добавить "))

D, L, R, I = 'data', 'left', 'right', 'index'
p = 0


def BinaryTree(tree, data, i):
    if tree is None:
        tree = {D: data, L: None, R: None, I: i}
    elif data <= tree[D]:
        tree[L] = BinaryTree(tree[L], data, i)
    else:
        tree[R] = BinaryTree(tree[R], data, i)
    return tree


tree = None
for i, el in enumerate(arr):
    tree = BinaryTree(tree, el, i)


def BinaryTreeSearch(tree):
    if value < tree[D] and tree[L] != None:
        BinaryTreeSearch(tree[L])
    elif value > tree[D] and tree[R] != None:
        BinaryTreeSearch(tree[R])
    elif value == tree[D]:
        print(tree[I])
    else:
        print("not found")


def BinaryTreeDelete(tree, arr, value):
    arr.pop(value)
    tree = None
    for i, el in enumerate(arr):
        tree = BinaryTree(tree, el, i)


def BinaryTreeAdd(tree, arr, val_a):
    arr.append(val_a)
    BinaryTree(tree, val_a, len(arr))


print("ячейка", BinaryTreeSearch(tree))

BinaryTreeDelete(tree, arr, value_add)
print("новый массив", arr)

BinaryTreeAdd(tree, arr, value_add)
print("новый массив", arr)



print("\nПоиск Фибоначчи\n")



arr = []
for i in range(15):
    arr.append(randint(1, 50))
arr.sort()
print(arr)


value = int(input("искать "))

value_delete = int(input("удалить "))

value_add = int(input("добавить "))


def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < val):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys) - 1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return i
    if (fibM_minus_1 and index < (len(lys) - 1) and lys[index + 1] == val):
        return index + 1;
    return "not found"


def FibonacciAdd(arr, val_a):
    arr.append(val_a)
    arr.sort()


def FibonacciDelete(arr, val_d):
    arr.pop(BinarySearch(arr, val_d))


print("ячейка", FibonacciSearch(arr, value))

FibonacciAdd(arr, value_add)
print("новый массив", arr)

FibonacciDelete(arr, value_delete)
print("новый массив", arr)

print("\nИнтерполяционный поиск\n")

arr = []
for i in range(15):
    arr.append(randint(1, 50))
arr.sort()
print(arr)


value = int(input("искать "))

value_delete = int(input("удалить "))

value_add = int(input("добавить "))


def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return "not found"


print("ячейка", InterpolationSearch(arr, value))


def InterpolationAdd(arr, val_a):
    arr.append(val_a)
    arr.sort()


def InterpolationDelete(arr, val_d):
    arr.pop(BinarySearch(arr, val_d))


print("Index =", FibonacciSearch(arr, value))

InterpolationAdd(arr, value_add)
print("новый массив", arr)

InterpolationDelete(arr, value_delete)
print("новый массив", arr)