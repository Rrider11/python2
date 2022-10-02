# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = input()

a = number.replace(".","")
b = a.replace(",","")
c = b.replace("-","")



res = [int(x) for x in str(c)]
# res = list(map(int, str(num))) вариант с "map"

# print(sum(res))
sum_d = 0
for i in res:
    
    sum_d += i
    

print(f"Сумма чисел равна: {sum_d}")






