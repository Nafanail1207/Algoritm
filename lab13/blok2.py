# Подсчет количества операций для вложенных циклов

def count_operations(n):
    count = 0
    for i in range(n):
        for j in range(i):
            count += 1
    return count

# Проверка
for n in [10, 100, 1000, 5000]:
    ops = count_operations(n)
    print(f"n={n}, операций={ops}, n^2={n*n}")