# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

a = int(input())

bin_ = []
while a > 0:
    bin_.append(a % 2)
    a = a // 2
print(bin_, end = "\n")

bin_ = list(reversed(bin_))
print(bin_)





