"""
📁 КОЛЛЕКЦИИ В PYTHON: СЛОВАРИ, МНОЖЕСТВА И ИХ ОБРАБОТКА
Данный файл содержит примеры работы с коллекциями и решения практических задач.
Автор: [Ваше имя]
Дата: [Дата]
"""

# ======================== 1. ОБЪЕДИНЕНИЕ СЛОВАРЕЙ ========================

def demonstrate_dict_merge():
    """Демонстрация методов объединения словарей"""
    print("\n=== 1. ОБЪЕДИНЕНИЕ СЛОВАРЕЙ ===")
    
    dict_1 = {1: 'a', 2: 'b'}
    dict_2 = {2: 'c', 4: 'd'}

    # Метод update()
    dict_1_copy = dict_1.copy()
    dict_1_copy.update(dict_2)
    print(f"Метод update():\n{dict_1_copy}")

    # Распаковка словарей (Python 3.9+)
    new_dict = {**dict_1, **dict_2}
    print(f"\nРаспаковка словарей:\n{new_dict}")

# ================= 2. ОБРАБОТКА СЛОВАРЕЙ: МАКСИМУМ И СУММА ================

from collections import defaultdict

def max_dict(*dicts):
    """Объединяет словари, выбирая максимальные значения для ключей"""
    merged = {}
    for d in dicts:
        for key, value in d.items():
            merged[key] = max(value, merged.get(key, value))
    return merged

def sum_dict(*dicts):
    """Суммирует значения для повторяющихся ключей"""
    summed = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            summed[key] += value
    return dict(summed)

def process_dictionaries():
    """Демонстрация работы с обработкой словарей"""
    print("\n=== 2. ОБРАБОТКА СЛОВАРЕЙ ===")
    
    dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
    dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
    dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
    dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

    print("Максимумы (dict1 + dict2):", max_dict(dict_1, dict_2))
    print("Суммы (dict1 + dict3 + dict4):", sum_dict(dict_1, dict_3, dict_4))
    print("Полные максимумы:", max_dict(dict_1, dict_2, dict_3, dict_4))
    print("Полные суммы:", sum_dict(dict_1, dict_2, dict_3, dict_4))

# ============== 3. ГЕНЕРАЦИЯ УНИКАЛЬНОГО МНОЖЕСТВА С ПРАВИЛАМИ =============

def set_gen(numbers):
    """Генерирует множество с особыми правилами преобразования"""
    count = {}
    result = []
    for num in numbers:
        count[num] = count.get(num, 0) + 1
        result.append(num if count[num] == 1 else str(num) * count[num])
    return set(result)

def demonstrate_set_generation():
    """Демонстрация генерации множеств"""
    print("\n=== 3. ГЕНЕРАЦИЯ МНОЖЕСТВ ===")
    
    lists = [
        [1, 1, 3, 3, 1],
        [5, 5, 5, 5, 5, 5, 5],
        [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
    ]
    
    for i, lst in enumerate(lists, 1):
        print(f"Список {i}: {set_gen(lst)}")

# ====================== 4. АНАЛИЗ СУПЕРМНОЖЕСТВ ========================

def superset(a, b):
    """Анализирует отношение множеств и выводит результат"""
    if a == b:
        print(f"Множества равны: {a} == {b}")
    elif a > b:
        print(f"Объект {a} является чистым супермножеством для {b}")
    elif b > a:
        print(f"Объект {b} является чистым супермножеством для {a}")
    else:
        print(f"Супермножество не обнаружено: {a} vs {b}")

def demonstrate_superset():
    """Демонстрация анализа множеств"""
    print("\n=== 4. АНАЛИЗ СУПЕРМНОЖЕСТВ ===")
    
    sets = [
        ({1, 8, 3, 5}, {3, 5}),
        ({1, 8, 3, 5}, {5, 3, 8, 1}),
        ({3, 5}, {5, 3, 8, 1}),
        ({90, 100}, {3, 5})
    ]
    
    for a, b in sets:
        superset(a, b)

# ======================= ЗАПУСК ВСЕХ ПРИМЕРОВ ========================

if __name__ == "__main__":
    demonstrate_dict_merge()      # Задание 1
    process_dictionaries()        # Задание 2
    demonstrate_set_generation()  # Задание 3
    demonstrate_superset()        # Задание 4
    print("\n✅ Все примеры выполнены!")
