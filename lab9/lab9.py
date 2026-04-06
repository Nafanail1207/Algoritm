# Класс узла
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Класс связного списка
class LinkedList:
    def __init__(self):
        self.head = None

    # Добавление в начало
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Добавление в конец
    def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # Вывод списка
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Поиск элемента
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Удаление первого элемента
    def delete_first(self):
        if self.head:
            self.head = self.head.next

    # Подсчет элементов
    def count(self):
        current = self.head
        c = 0
        while current:
            c += 1
            current = current.next
        return c

    # Разворот списка
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


# ===== Основная программа =====

ll = LinkedList()

print("Введите 5 чисел:")

for i in range(5):
    num = int(input())
    ll.add_last(num)

print("Список:")
ll.print_list()

print("Количество элементов:", ll.count())

# Поиск
value = int(input("Введите число для поиска: "))
print("Найдено:", ll.search(value))

# Удаление первого
print("Удаляем первый элемент...")
ll.delete_first()
ll.print_list()

# Разворот
print("Разворот списка:")
ll.reverse()
ll.print_list()