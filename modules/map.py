# Se transformo el array 1
numbers = [1,2,3,4]

numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)
    
print(numbers)
print(numbers_v2)



# Ahora la misma transformacion en una linea 
#usando lambdas y map

number_map = list(map(lambda i : i*2, numbers))
print(number_map) 

#Ejemplo2

number_1 = [1,2,3,4]
number_2 = [5,6,7]
number_map_v2 = list(map(lambda x, y : x + y, number_1, number_2))
print(number_map_v2)