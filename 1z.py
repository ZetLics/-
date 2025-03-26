#1
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_1.update(dict_2)
print(dict_1)
new_dict = {**dict_1, **dict_2}
print(new_dict)

#-----------------------------------------------------------------
#2
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

#print({**dict_1, **dict_2, **dict_3, **dict_4})
#print(dict_1|dict_2|dict_3|dict_4)

from collections import defaultdict

def max_dict(*dicts):
    merged = {}
    for d in dicts:
        for key, value in d.items():
            merged[key] = max(value, merged.get(key, value))
    return merged

def sum_dict(*dicts):
    summed = defaultdict(int)
    for d in dicts:
        for key, value in d.items():
            summed[key] += value
    return dict(summed)

print(max_dict(dict_1, dict_2))
print(sum_dict(dict_1, dict_4, dict_3))
print(max_dict(dict_1, dict_2, dict_3, dict_4))
print(sum_dict(dict_1, dict_2, dict_3, dict_4))

#-----------------------------------------------------------------
#3
def set_gen(numbers):
    count = {}
    result = []
    for num in numbers:
        count[num] = count.get(num, 0) + 1
        if count[num] == 1:
            result.append(num)
        else:
            result.append(str(num) * count[num])
    return set(result)

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))

#-----------------------------------------------------------------
#4
def superset(a, b):
    if a == b:
        print("Множества равны")
    elif a > b:
        print(f"Объект {a} является чистым супермножеством")
    elif b > a:
        print(f"Объект {b} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}

superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)