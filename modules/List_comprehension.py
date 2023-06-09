number = []
for element in range(1,11):
    number.append(element)
    
print(number)
    

#Aplicando list comprehension 

numbers = [elemento for elemento in range(1,11)]
print(numbers)


#Ejemplo 2
number = []
for element in range(1,11): 
    if element % 2 == 0:
        number.append(element*2)
    
print(number)

#Aplicando list comprehension 
number_par = [i * 2 for i in range(1,11) if i % 2 == 0]
print(number_par)