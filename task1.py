#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#и проверяет, является ли этот день выходным.
#*Пример:*

#- 6 -> да
#- 7 -> да
#- 1 -> нет

print("Введите число от 1 до 7 ")
day = int(input())

if 0 < day < 6:
    print('Wake up son')
elif 5 < day < 8:
    print('all together sleep')
else:
    print("its not a weekday")
    
