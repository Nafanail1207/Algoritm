from collections import deque

# -------------------------
# 1. TO-DO LIST
# -------------------------
tasks = []

def todo():
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Добавить")
        print("2. Удалить")
        print("3. Показать")
        print("0. Назад")

        c = input("> ")

        if c == "1":
            tasks.append(input("Задача: "))
        elif c == "2":
            for i, t in enumerate(tasks):
                print(i, t)
            i = int(input("Индекс: "))
            if 0 <= i < len(tasks):
                tasks.pop(i)
        elif c == "3":
            print(tasks)
        elif c == "0":
            break


# -------------------------
# 2. STACK CALCULATOR (упрощённый)
# -------------------------
def calc():
    expr = input("Введите выражение: ")
    print("Результат (eval):", eval(expr))


# -------------------------
# 3. QUEUE
# -------------------------
def queue_app():
    q = deque()

    while True:
        print("\n--- QUEUE ---")
        print("1. Добавить")
        print("2. Обработать")
        print("3. Показать")
        print("0. Назад")

        c = input("> ")

        if c == "1":
            q.append(input("Клиент: "))
        elif c == "2":
            print("Обслужен:", q.popleft() if q else "Пусто")
        elif c == "3":
            print(list(q))
        elif c == "0":
            break


# -------------------------
# 4. TEXT ANALYSIS
# -------------------------
def text_analysis():
    text = input("Текст: ").lower().split()
    freq = {}

    for w in text:
        freq[w] = freq.get(w, 0) + 1

    print("Слова:", len(text))
    print("Повторы:", {k:v for k,v in freq.items() if v > 1})


# -------------------------
# 5. LINKED LIST
# -------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, v):
        n = Node(v)
        if not self.head:
            self.head = n
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n

    def show(self):
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")


def linked_list_app():
    ll = LinkedList()

    while True:
        print("\n--- LINKED LIST ---")
        print("1. Добавить")
        print("2. Показать")
        print("0. Назад")

        c = input("> ")

        if c == "1":
            ll.add(input("Значение: "))
        elif c == "2":
            ll.show()
        elif c == "0":
            break


# -------------------------
# 6. PHONE BOOK
# -------------------------
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.next = None

class PhoneBook:
    def __init__(self):
        self.head = None

    def add(self, n, p):
        c = Contact(n, p)
        c.next = self.head
        self.head = c

    def find(self, n):
        cur = self.head
        while cur:
            if cur.name == n:
                return cur.phone
            cur = cur.next
        return "Не найден"


def phone_app():
    pb = PhoneBook()

    while True:
        print("\n--- PHONE BOOK ---")
        print("1. Добавить")
        print("2. Найти")
        print("0. Назад")

        c = input("> ")

        if c == "1":
            pb.add(input("Имя: "), input("Телефон: "))
        elif c == "2":
            print(pb.find(input("Имя: ")))
        elif c == "0":
            break


# -------------------------
# 7–9 TREE (упрощённо)
# -------------------------
class T:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def tree_app():
    root = T(1)
    root.l = T(2)
    root.r = T(3)

    print("\nTree:")
    print(root.v, root.l.v, root.r.v)


# -------------------------
# 10 GRAPH
# -------------------------
graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"]
}

def graph_app():
    print(graph)


# -------------------------
# 11 DFS
# -------------------------
def dfs(v, vis):
    vis.add(v)
    print(v)
    for n in graph[v]:
        if n not in vis:
            dfs(n, vis)

def dfs_app():
    dfs("A", set())


# -------------------------
# 12 BFS
# -------------------------
def bfs_app():
    q = deque(["A"])
    vis = set()

    while q:
        v = q.popleft()
        if v not in vis:
            print(v)
            vis.add(v)
            q.extend(graph[v])


# -------------------------
# 13 SHORTEST PATH
# -------------------------
def shortest():
    q = deque([("A", ["A"])])
    vis = set()

    while q:
        v, path = q.popleft()
        if v == "C":
            print(path)
            return
        for n in graph[v]:
            if n not in vis:
                vis.add(n)
                q.append((n, path + [n]))


# -------------------------
# 14 NAVIGATION
# -------------------------
def nav():
    print("Маршрут:", ["A", "B", "C"])


# -------------------------
# 15 SEARCH ENGINE
# -------------------------
def search_engine():
    web = {
        "home": ["about"],
        "about": ["team"],
        "team": []
    }
    print(web)


# -------------------------
# MAIN MENU
# -------------------------
while True:
    print("\n========================")
    print(" SRO 2 MENU")
    print("========================")
    print("1. To-Do List")
    print("2. Calculator")
    print("3. Queue")
    print("4. Text Analysis")
    print("5. Linked List")
    print("6. Phone Book")
    print("7. Tree")
    print("8. Graph")
    print("9. DFS")
    print("10. BFS")
    print("11. Shortest Path")
    print("12. Navigation")
    print("13. Search Engine")
    print("0. Exit")

    c = input("> ")

    if c == "1": todo()
    elif c == "2": calc()
    elif c == "3": queue_app()
    elif c == "4": text_analysis()
    elif c == "5": linked_list_app()
    elif c == "6": phone_app()
    elif c == "7": tree_app()
    elif c == "8": graph_app()
    elif c == "9": dfs_app()
    elif c == "10": bfs_app()
    elif c == "11": shortest()
    elif c == "12": nav()
    elif c == "13": search_engine()
    elif c == "0": break