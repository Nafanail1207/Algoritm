from collections import deque

# Задача 1 & 2: Создание графа (список смежности) и добавление вершины
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']  # Новая вершина (Задача 2)
}

# Задача 3: Функция для вывода соседей
def get_neighbors(graph, node):
    return graph.get(node, [])

# Задача 4: DFS (рекурсивный)
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

# Задача 5: DFS (через стек)
def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Добавляем соседей в обратном порядке, чтобы обход был идентичен рекурсии
            stack.extend(reversed(graph[node]))
    return order

# Задача 6: BFS (через очередь)
def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# Задача 8: Проверка существования пути
def has_path(graph, start, end):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end: return True
        if node not in visited:
            visited.add(node)
            queue.extend(n for n in graph[node] if n not in visited)
    return False

# Задача 9: Количество достижимых вершин
def count_reachable(graph, start):
    return len(bfs(graph, start))

# Задача 10: Кратчайший путь (BFS)
def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (node, path) = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Задача 7: Демонстрация работы
start_node = 'A'
print(f"Обход в ширину (BFS) от {start_node}:", bfs(graph, start_node))
print(f"Кратчайший путь A -> F:", shortest_path(graph, 'A', 'F'))
