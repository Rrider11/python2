# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input())

list_nums = []
sum_nums = 0

for i in range(1, n+1):
    result = round((1 + 1/n) ** n )
    list_nums.append(result)
    sum_nums += result

print(list_nums)
print(sum_nums)
