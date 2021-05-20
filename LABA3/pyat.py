from queue import PriorityQueue

N = 4


# Движение пятнашек
def moves(position):
    blank = position.index(0)
    i, j = divmod(blank, N)
    offsets = []
    if i > 0: offsets.append(-N)  # вниз
    if i < N - 1: offsets.append(N)  # вверх
    if j > 0: offsets.append(-1)  # вправо
    if j < N - 1: offsets.append(1)  # влево
    for offset in offsets:
        swap = blank + offset
        yield tuple(
            position[swap] if x == blank else position[blank] if x == swap else position[x] for x in range(N * N))


# Функция для определения есть решение или нет
def parity(permutation):
    seen, cycles = set(), 0
    for i in permutation:
        if i not in seen:
            cycles += 1
            while i not in seen:
                seen.add(i)
                i = permutation[i]
    return (cycles + len(permutation)) % 2


# Класс позиции
class Position:
    # Конструктор класса, который принимает позицию и начальную дистанцию
    def __init__(self, position, start_distance):
        self.position = position
        self.start_distance = start_distance

    # Метод, который срабатывает при сравнении (<) объектта с другим объектом
    def __lt__(self, other):
        return self.start_distance < other.start_distance

    # Метод, который срабатывает при использовании объекта как строки
    def __str__(self):
        return '\n'.join((N * '{:3}').format(*[i % (N * N) for i in self.position[i:]]) for i in range(0, N * N, N))


# Разгадка
SOLVED = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)
# Загадка
start = [1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0]

# Смотрим, можно ли в данной расстановке найти решение
# Если нет, то сообщаем об этом
if parity(start) == 0:
    print('Нерешаемо')
# Иначе ищем этот путь
else:

    start = tuple(start)

    # Первоначальная позиция
    p = Position(start, 0)
    print("Первоначальная позиция: " + "\n", p)
    print()

    # 1) Кладем в очередь с приоритетом первоначальную позицию
    candidates = PriorityQueue()
    candidates.put(p)

    # Кортеж посещенных позиций
    visited = set([p])

    # Откуда пришли
    came_from = {p.position: None}

    # Пока решение не найдено
    while p.position != SOLVED:
        # 2) Извлекаем из очереди позицию с наименьшим приоритетом
        p = candidates.get()
        # 3) Кладем в очередь все соседние позиции
        # 4) Повторяем пункты 2-4 пока в пункте 2 не вытащим конечную позицию
        for k in moves(p.position):
            if k not in visited:
                # В candifates хранятся всевозможные позиции
                candidates.put(Position(k, p.start_distance + 1))
                came_from[k] = p
                visited.add(k)

    # path - последовательное решение головоловки (путь)
    path = []
    # Сохраняем конечную позицию
    prev = p
    # Идем в обратном порядке и запоминаем очередность хода в path
    while p.position != start:
        # Запоминаем откуда ход
        p = came_from[p.position]
        number = p.position[prev.position.index(0)]
        path.append(number)
        prev = p
    path.reverse()

    print("Оптимальный путь к решению:" + "\n", path)