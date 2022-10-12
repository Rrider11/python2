# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

arr = [1.1, 1.2, 3.1, 5, 10.01]
arr1 = [x for x in arr if type(x) != int]
print(arr1)


arr2 = []
for i in range(len(arr1)):
    arr2.append(round(arr1[i] % 1, 2))
    
print(arr2)

max_1 = max(arr2)
min_1 = min(arr2)
print(max_1 - min_1)