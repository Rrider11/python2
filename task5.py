#5. Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
#in
#- 3
#- 6
#- 2
#- 1

#out
#5.099

print('Введите координаты двух точек по оси x и y')
dot1x = int(input())
dot1y = int(input())

dot2x = int(input())
dot2y = int(input())

len_x_y = ((dot2x - dot1x) ** 2 + (dot2y - dot1y) ** 2) ** 0.5
print(len_x_y)
