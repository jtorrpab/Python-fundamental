
import random
countries= ['col','per','arg','ecu']
population2={country: random.randint(1,100) for country in countries}
print(population2)

    
result = {country : population for (country, population) in population2.items() if population > 20}
print(result)


#Ejemplo 2
text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)