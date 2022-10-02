# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]



# using random.sample()
 
import random
 
test_list = [1, 4, 5, 6, 3]
 
print ("The original list is : " + str(test_list))
 
res = random.sample(test_list, len(test_list))
 
print ("The shuffled list is : " +  str(res))