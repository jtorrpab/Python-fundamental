dict = {}
for i in range (1,11):
    dict[i] = i* 2
    
print(dict)

#Dictionary comprehension 
dict_2 = { i: i * 2 for i in range(1,11) }

import random
countries = ['col','per','arg','ecu']
population={}
for country in countries:
    population[country] = random.randint(1,100)
    
print(population)


#Dictionary comprehension 
countries2= ['col','per','arg','ecu']
population2={country: random.randint(1,100) for country in countries}
print(population2)


names = ['Nico','Zule','Santi']
ages = [12,56,98]
print(list(zip(names,ages)))

new_dcit={name : age for (name, age) in zip(names,ages)}
print(new_dcit)