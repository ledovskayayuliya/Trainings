Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_code = goods['Стол']
tables_item_1 = store[table_code][0]
tables_item_2 = store[table_code][1]
tables_quantity = tables_item_1['quantity'] + tables_item_2['quantity']
tables_price = tables_item_1['price'] + tables_item_2['price']
tables_cost = tables_quantity * tables_price
print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')

sofa_code = goods['Диван']
sofas_item_1 = store[sofa_code][0]
sofas_item_2 = store[sofa_code][1]
sofas_quantity = sofas_item_1['quantity'] + sofas_item_2['quantity']
sofas_price = sofas_item_1['price'] + sofas_item_2['price']
sofas_cost = sofas_quantity * sofas_price
print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')

chair_code = goods['Стул']
chairs_item_1 = store[chair_code][0]
chairs_item_2 = store[chair_code][1]
chairs_item_3 = store[chair_code][2]
chairs_quantity = chairs_item_1['quantity'] + chairs_item_2['quantity'] + chairs_item_3['quantity']
chairs_price = chairs_item_1['price'] + chairs_item_2['price'] + chairs_item_3['price']
chairs_cost = chairs_quantity * chairs_price
print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')




