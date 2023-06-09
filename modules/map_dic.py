items = [
    {
        'producto' : 'camisa',
        'price' : 100
    },
    {
        'producto' : 'pantalones',
        'price' : 300
    },
    {
        'producto' : 'gorra',
        'price' : 50
    },
    {
        'producto' : 'chaqueta',
        'price' : 500
    },
]

print('Diccionario principal')
print(items)

price = list(map(lambda item: item['price'], items))
print('Lista de precios ')
print(price)

def add_taxes(items):
    new_item = items.copy()
    new_item['taxes'] = items['price'] * .19
    return new_item

new_item = list(map(add_taxes, items))
print('Diccionario nuevo')
print(new_item)