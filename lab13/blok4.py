import sys
import time
import tracemalloc

# ------------------ Пример графа (в виде списка смежности) ------------------
def create_graph(n):
    graph = {i: [i + 1] for i in range(n - 1)}
    graph[n - 1] = []
    return graph

# ------------------ DFS (рекурсивный) ------------------
def dfs_recursive(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# ------------------ DFS (через стек) ------------------
def dfs_stack(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    
    return visited

# ------------------ Замер памяти ------------------
def measure_memory(func, *args):
    tracemalloc.start()
    start = time.perf_counter()
    
    func(*args)
    
    end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return end - start, peak

# ------------------ Тест ------------------
def main():
    n = 10000  # размер графа (можно увеличить)
    graph = create_graph(n)
    
    # Рекурсия
    visited = set()
    rec_time, rec_memory = measure_memory(dfs_recursive, graph, 0, visited)
    
    # Стек
    stack_time, stack_memory = measure_memory(dfs_stack, graph, 0)
    
    print("=== DFS сравнение ===")
    print(f"Рекурсия: время = {rec_time:.6f}s, память = {rec_memory / 1024:.2f} KB")
    print(f"Стек:     время = {stack_time:.6f}s, память = {stack_memory / 1024:.2f} KB")
    
    print("\nПримечание:")
    print("- Рекурсия использует стек вызовов (ограничен, возможен RecursionError)")
    print("- Явный стек управляется вручную и обычно стабильнее по памяти")

if __name__ == "__main__":
    main()