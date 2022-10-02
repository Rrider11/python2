# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов,
#  заполненных числами из промежутка [-N, N]. 
#  Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

N = int(input())
pos_1 = int(input())
pos_1_1 = pos_1 - 1
pos_2 = int(input())
pos_2_2 = pos_2 - 1
num_list = []
for i in range(-N, N + 1):
    num_list.append(i)
print(num_list[pos_1_1] * num_list[pos_2_2])


