# Лабораторная работа №12: Хеширование (Python)

# 1-3. Создание словаря и вывод элементов
students = {
    101: "Кириленко Григорий",
    102: "Кератинов Роман",
    103: "Сидоров Сидор",
    104: "Мандаева Ельвира"
}
print("1-3. Исходный словарь студентов:", students)

# 4. Проверка существования ключа
key_to_check = 102
if key_to_check in students:
    print(f"4. Студент с ID {key_to_check} найден: {students[key_to_check]}")

# 5. Удаление элемента по ключу
removed_student = students.pop(103)
print(f"5. Удален студент: {removed_student}. Обновленный словарь: {students}")

# 6. Очистка словаря
temp_dict = students.copy()
temp_dict.clear()
print("6. Словарь после очистки clear():", temp_dict)

# 7. Работа с множествами (set)
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"7. Множество A: {set_a}, Множество B: {set_b}")

print("8. Объединение:", set_a | set_b)
print("   Пересечение:", set_a & set_b)
print("   Разность (A-B):", set_a - set_b)
set_a.add(10)
set_a.discard(1) # удаляет 1, если она есть
print("9. Множество A после изменений:", set_a)

class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self._hash_function(key)
        return self.table[index]

hash_tab = SimpleHashTable(10)
hash_tab.insert("user1", "Admin")
print(f"10. Данные из хеш-таблицы по ключу 'user1': {hash_tab.get('user1')}")
