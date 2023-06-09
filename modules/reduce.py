import functools

number = [1,2,3,4]

result = functools.reduce(lambda counter, item: counter + item, number)
print(result)

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, number)

print(result)