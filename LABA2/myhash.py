import random

print("\nПростое рехеширование\n")


class prost_rehash:
    # Конструктор, создание словаря
    def __init__(self):
        self.rhash = [None] * 256

    def keys(self, element):
        key = 0
        for i in range(len(element)):
            key = key + ord(element[i])
        return int(key % 256)

    def add(self, element):
        key = self.keys(element)
        while self.rhash[key] is not None:
            key = key + 1
        self.rhash[key] = element

    def search(self, element):
        key = self.keys(element)
        while self.rhash[key] is not None:
            if self.rhash[key] == element:
                return key
            else:
                key = key + 1
        return None

    def deleted(self, element):
        key = self.search(element)
        while key is not None and self.rhash[key] is not None:
            if self.rhash[key] == element:
                del self.rhash[key]
                key = int(key + 1)
                while key < len(self.rhash) and self.rhash[key] is not None:
                    el = self.rhash.pop(key)
                    self.add(el)
                    key = key + 1
                return 1
            else:
                key = key + 1
        return -1

    def pr(self):
        for key, i in enumerate(self.rhash):
            if self.rhash[key] is not None:
                print(key, " ", i)


a = prost_rehash()
a.add("qwe")
a.add("qwq")
a.add("qws")
a.add("qwm")
a.add("qwo")
a.pr()
s = a.deleted("qwq")
print(s)
a.pr()

print("\nРехэширование с помощью псевдослучайных чисел\n")


class random_rehash():

    def __init__(self):
        self.rhash = [None] * 256

    def rand(self, element):
        key = int(0)
        for i in range(len(element)):
            key = key + ord(element[i])
        return key

    def keys(self, key, l):
        random.seed(l)
        return int(key + ((random.random() * 10000000000000000) % 1000))

    def add(self, element):
        l = int(0)
        key = self.rand(element)
        key1 = self.keys(key, l) % 256
        while key1 < len(self.rhash) and self.rhash[key1] is not None:
            l = l + 1
            key1 = self.keys(key, l) % 256
        if key1 < len(self.rhash):
            self.rhash[key1] = element
        else:
            print("Таблица заполнена")

    def search(self, element):
        l = int(0)
        key = self.rand(element)
        key1 = self.keys(key, l) % 256
        while key1 < len(self.rhash) and self.rhash[key1] is not None:
            if self.rhash[key1] == element:
                return key1
            else:
                l = l + 1
                key1 = self.keys(key, l)
        return None

    def deleted(self, element):
        l = int(0)
        keyn = self.rand(element)
        key1 = self.keys(keyn, l) % 256
        key = self.search(element)
        if key is not None:
            while key is not key1:
                l = l + 1
                key1 = self.keys(keyn, l) % 256
                self.rhash[key] = None
                l = l + 1
                key1 = self.keys(keyn, l) % 256
            while key1 < len(self.rhash) and self.rhash[key1] is not None:
                el = self.rhash[key1]
                self.rhash[key1] = None
                self.add(el)
                l = l + 1
                key1 = self.keys(keyn, l) % 256
            return "Элемент удален"
        else:
            return "Элемент не найден"

    def pr(self):  #
        for key, i in enumerate(self.rhash):
            if self.rhash[key] is not None:
                print(key, " ", i)


a = random_rehash()
a.add("qwe")
a.add("qwe")
a.add("qwe")
a.add("qwe")
a.add("qwe")
a.pr()
s = a.deleted("qwe")
print(s)
a.pr()
print(a.search("qwe"))

print("\nМетод цеопчек\n")


class chain_rehash:

    def __init__(self):
        self.rhash = [[] * 0 for i in range(10)]

    def add(self, element):
        key = int(0)
        for i in range(len(element)):
            key = key + ord(element[i])
        key = key % 10
        self.rhash[key].append(element)

    def search(self, element):
        key = int(0)
        for i in range(len(element)):
            key = key + ord(element[i])
        key = key % 10
        if self.rhash[key] is not None:
            for i in range(len(self.rhash[key])):
                if self.rhash[key][i] == element:
                    return key, i
        return None, None

    def deleted(self, element):
        key, i = self.search(element)
        if key is not None:
            del (self.rhash[key][i])
            print("Элемент успешно удален")
        else:
            print("Элемент не найден")
            return -1

    def pr(self):  # вывод
        for key in range(len(self.rhash)):
            for i in range(len(self.rhash[key])):
                if self.rhash[key][i] is not None:
                    print("(ключ)", key, "- (Элемент)", self.rhash[key][i])


a = chain_rehash()
a.add("qwe")
a.add("qwe")
a.add("qwe")
a.pr()
a.deleted("qwe")
a.pr()