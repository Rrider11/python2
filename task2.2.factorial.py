# 2. Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N.

# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]


# print("Напишите число")
# N = int(input())
# sum_N = 1

# for i in range(N):
#     sum_N *= i + 1
#     print(sum_N, end = ", ")

n = int(input())
 
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
    print(factorial, end = ", ")


