# -*- coding: utf-8 -*-
import random

class LinkedNode:
    # Связный список с ссылками на предыдущий и следующий элемент
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


class Stack:
    def __init__(self):
        self.head = LinkedNode()
        self.size = 0

    # Проверка на пустату
    def is_empty(self):
        return self.size == 0

    # Добавление
    def push(self, value):
        if self.size > 0:
            node = LinkedNode(value)
            node.right = self.head
            self.head = node
        else:
            self.head.value = value
        self.size += 1

    # Удаление
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove = self.head
        if self.size > 1:
            self.head = remove.right
        self.size -= 1
        return remove.value

    def peek(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        return self.head.value

    def __len__(self):
        return self.size

    def reverse(self):
        current = self.head
        prev = None
        next = None

        while current is not None:
            next = current.right
            current.right = prev
            prev = current
            current = next

        self.head = prev


class Deque:
    def __init__(self):
        self.head = LinkedNode()
        self.tail = self.head
        self.size = 0

    # Проверка на пустату
    def is_empty(self):
        return self.size == 0

    # Добавление в конец
    def push_left(self, value):
        if self.size > 0:
            node = LinkedNode(value)
            node.right = self.tail
            self.tail.left = node
            self.tail = node
        else:
            self.tail.value = value
        self.size += 1

    # Добавление в начало
    def push(self, value):
        if self.size > 0:
            node = LinkedNode(value)
            node.left = self.head
            self.head.right = node
            self.head = node
        else:
            self.head.value = value
        self.size += 1

    # Удаление в конец
    def pop_left(self):
        if self.is_empty():
            raise Exception("Popping from an empty deque")
        remove = self.tail
        if self.size > 1:
            self.tail = remove.right
        self.size -= 1
        return remove.value

    # Удаление в начале
    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty deque")
        remove = self.head
        if self.size > 1:
            self.head = remove.left
        self.size -= 1
        return remove.value

    def peek(self):
        if self.is_empty():
            raise Exception("Popping from an empty deque")
        return self.head.value

    def peek_left(self):
        if self.is_empty():
            raise Exception("Popping from an empty deque")
        return self.tail.value

    def __len__(self):
        return self.size

#Задание 1
print("\nЗадание №1\n")
with open('books.txt', 'r') as books:
    d1 = Deque()
    d2 = Deque()
    for book in books:
        d1.push(book)
    while not d1.is_empty():
        a = d1.pop()
        while not d2.is_empty() and d2.peek() > a:
            d1.push_left(d2.pop())
        d2.push(a)
    while not d2.is_empty():
        print(d2.pop_left())

#Задание 2
print("\nЗадание №2\n")

alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
random.shuffle(alphabet)
alphabet = ''.join(alphabet)
print(alphabet)
keyRing = Deque()
for letter in alphabet:
    keyRing.push(letter)


def encode_char(c):
    for i in range(len(keyRing)):
        x = keyRing.pop_left()
        if x == c:
            keyRing.push(x)
            val = keyRing.pop_left()
            keyRing.push(val)
            return val
        keyRing.push(x)


def decode_char(c):
    for i in range(len(keyRing)):
        x = keyRing.pop()
        if x == c:
            keyRing.push_left(x)
            val = keyRing.pop()
            keyRing.push_left(val)
            return val
        keyRing.push_left(x)


text = 'Я помню чудное мгновенье: передо мной явилась ты, как мимолетное виденье, как гений чистой красоты. В томленьях грусти безнадежной, в тревогах шумной суеты, звучал мне долго голос нежный и снились милые черты.'.lower()
encoded = ''
for letter in text:
    if encoded_letter := encode_char(letter):
        encoded += encoded_letter
    else:
        encoded += letter

print(encoded)

decoded = ''
for letter in encoded:
    if decoded_letter := decode_char(letter):
        decoded += decoded_letter
    else:
        decoded += letter
print(decoded)
#Задание 3
print("\nЗадание №3\n")
A = Stack()
B = Stack()
C = Stack()

disks = 10

for i in range(disks, 0, -1):
    A.push(i)

def move(a, b):
    if len(a) == 0 and len(b) > 0:
        a.push(b.pop())
    elif len(a) > 0 and len(b) == 0:
        b.push(a.pop())
    elif a.peek() > b.peek():
        a.push(b.pop())
    else:
        b.push(a.pop())

if disks % 2 == 0:
    while len(C) != disks:
        move(A, B)
        move(A, C)
        move(B, C)
else:
    while len(C) != disks:
        move(A, C)
        move(A, B)
        move(B, C)

while not C.is_empty():
    print(C.pop())
#Задание 4
print("\nЗадание №4\n")
def check_brackets(string):
    bracket_stack = Stack()
    for i in string:
        if i == '(':
            bracket_stack.push(i)
        elif i == ')':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
    return bracket_stack.is_empty()

print(check_brackets('()())((())(()(())()'))
print(check_brackets('(()())()()()()(()(()(())()))'))
#Задание 5
print("\nЗадание №5\n")
check = Deque()

with open('scobki.txt', 'r') as brackets:
    while True:
        char = brackets.read(1)
        if not char:
            break

        if char == '[':
            check.push(char)
        elif char == ']':
            if check.is_empty():
                break
            check.pop()

if check.is_empty():
    print('Скобок хватает')
else:
    print('Скобок не хватает')
#Задание 6
print("\nЗадание №6\n")
letters = Stack()
digits = Stack()
others = Stack()
result = ''

with open('alf.txt', 'r') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if c.isalpha():
            letters.push(c)
        elif c.isdigit():
            digits.push(c)
        else:
            others.push(c)

    letters.reverse()
    digits.reverse()
    others.reverse()

    while not digits.is_empty():
        result += digits.pop()
    while not letters.is_empty():
        result += letters.pop()
    while not others.is_empty():
        result += others.pop()

print(result)
#Задание 7
print("\nЗадание №7\n")
numbers = [random.randint(-10, 10) for i in range(10)]
print(numbers)

deque = Deque()
for n in numbers:
    if n < 0:
        deque.push_left(n)
    else:
        deque.push(n)

while not deque.is_empty():
    x = deque.pop_left()
    if x < 0:
        deque.push(x)
    else:
        deque.push_left(x)
        break

while not deque.is_empty():
    x = deque.pop()
    if x < 0:
        print(x)
    else:
        deque.push(x)
        break

while not deque.is_empty():
    print(deque.pop_left())
#Задание 8
print("\nЗадание №8\n")
with open('obr.txt', 'r') as family:
    stack = Stack()
    for member in family:
        print(member)
        stack.push(member)
    print()
    while not stack.is_empty():
        print(stack.pop())
#Задание 9
print("\nЗадание №9\n")
text = 'N((TXF)AF)OT'

opstack = Stack()
vstack = Stack()

cur = 0
while True:
    read = False
    if not opstack.is_empty():
        if opstack.peek() == 'N':
            if vstack.is_empty():
                read = True
            else:
                if vstack.pop() == 'T':
                    vstack.push('F')
                else:
                    vstack.push('T')
                opstack.pop()
        elif opstack.peek() == 'A':
            if len(vstack) < 2:
                read = True
            else:
                a = vstack.pop()
                b = vstack.pop()
                if a == b and b == 'T':
                    vstack.push('T')
                else:
                    vstack.push('F')
                opstack.pop()
        elif opstack.peek() == 'O':
            if len(vstack) < 2:
                read = True
            else:
                a = vstack.pop()
                b = vstack.pop()
                if a == 'T' or b == 'T':
                    vstack.push('T')
                else:
                    vstack.push('F')
                opstack.pop()
        elif opstack.peek() == 'X':
            if len(vstack) < 2:
                read = True
            else:
                a = vstack.pop()
                b = vstack.pop()
                if a != b:
                    vstack.push('T')
                else:
                    vstack.push('F')
                opstack.pop()
        elif opstack.peek() == '(':
            read = True
        elif opstack.peek() == ')':
            opstack.pop()
            opstack.pop()
    else:
        read = True
    if read:
        i = text[cur]
        if i in 'FT':
            vstack.push(i)
        if i in 'AXON()':
            opstack.push(i)
        cur += 1

    if cur == len(text) and len(opstack) == 0:
        break

while not vstack.is_empty():
    print(vstack.pop())
#Задание 10
print("\nЗадание №10\n")
text = 'M(5, M(8, N(4, N(1, M(7, N(5, 3))))))'

op = Stack()
nums = Stack()

num = ''

cur = 0
while cur < len(text):
    i = text[cur]
    if i.isdigit():
        num += i
    elif num != '':
        nums.push(int(num))
        num = ''
    if i in 'MN':
        op.push(i)
    cur += 1

while not op.is_empty():
    a = nums.pop()
    b = nums.pop()
    if a < b:
        a,b = b,a
    if op.pop() == 'M':
        nums.push(a)
    else:
        nums.push(b)

while not nums.is_empty():
    print(nums.pop())

#Задание 11
print("\nЗадание №11\n")
def check(text):
    stack = Stack()

    cur = 0
    while True:
        read = False
        if not stack.is_empty():
            if stack.peek() == '(':
                read = True
            elif stack.peek() == ')':
                stack.pop()
                if len(stack) < 2 or stack.pop() != 'formula' or stack.pop() != '(':
                    return False
                stack.push('formula')
            elif stack.peek() == 'formula':
                stack.pop()
                if len(stack) > 1 and stack.peek() in '+-':
                    if stack.pop() in '+-' and stack.pop() == 'formula':
                        stack.push('formula')
                    else:
                        return False
                else:
                    stack.push('formula')
                    read = True
            else:
                read = True
        else:
            read = True
        if read:
            i = text[cur]
            if i in 'xyz':
                stack.push('formula')
            elif i in '()+-':
                stack.push(i)
            cur += 1
        if cur == len(text) and len(stack) == 1:
            break
    return True

print(check('(x + y) - (x + ) - z'))