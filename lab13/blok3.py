import time

# --- Наивная рекурсия ---
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# --- Итеративный подход ---
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# --- Замер времени ---
def measure():
    print("n | recursion_time | iteration_time")
    print("-" * 40)
    
    for n in range(1, 45):
        # Итерация
        start = time.perf_counter()
        fib_iterative(n)
        iter_time = time.perf_counter() - start
        
        # Рекурсия
        start = time.perf_counter()
        fib_recursive(n)
        rec_time = time.perf_counter() - start
        
        print(f"{n:2d} | {rec_time:.6f}s | {iter_time:.6f}s")
        
        # условие "зависания" (например > 1 сек)
        if rec_time > 1:
            print(f"\n⚠️ Рекурсия начинает 'зависать' примерно при n ≈ {n}")
            break

if __name__ == "__main__":
    measure()