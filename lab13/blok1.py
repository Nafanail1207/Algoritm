import time
import random
import matplotlib.pyplot as plt

# --- Линейный поиск ---
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# --- Бинарный поиск ---
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# --- Размеры массивов ---
sizes = [100, 1000, 10000, 100000, 500000, 1000000]

linear_times = []
binary_times = []

for n in sizes:
    arr = list(range(n))  # отсортированный массив
    target = n - 1        # худший случай для линейного поиска
    
    # --- Линейный поиск ---
    start = time.time()
    linear_search(arr, target)
    end = time.time()
    linear_times.append(end - start)
    
    # --- Бинарный поиск ---
    start = time.time()
    binary_search(arr, target)
    end = time.time()
    binary_times.append(end - start)

# --- График ---
plt.figure(figsize=(10, 6))
plt.plot(sizes, linear_times, label="Линейный поиск", marker='o')
plt.plot(sizes, binary_times, label="Бинарный поиск", marker='o')

plt.xlabel("Размер массива (n)")
plt.ylabel("Время (сек)")
plt.title("Сравнение линейного и бинарного поиска")
plt.legend()
plt.grid(True)

plt.xscale("log")  # удобно для больших n
plt.yscale("log")

plt.show()