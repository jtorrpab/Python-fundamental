# Esta función tiene parametros de entrada, pero no retorna nada por lo que tiene la funcion print para mostrar el resultado
def sum_with_range(a:int, b:int ):
    print ("Sin return")
    sum = 0
    for x in range(a,b):
        sum +=x    
    print(sum)
print(sum_with_range(1,10))

#Ahora vamos a retornar el resultado, así.
def sum_with_range2(a:int, b:int ):
    print ("Con return")
    sum = 0
    for x in range(a,b):
        sum +=x    
    return sum

result = sum_with_range2(1,10)
print(result)


def find_volume(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)