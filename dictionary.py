dic = {'item1': 100, 'item2': 200, 'item3': 300}

# access
print(dic['item1']) # 100

# add
dic['item4'] = 400
print(dic)  # item1:100, item2:200, item3:300, item4:400

# update
dic['item1'] = 120
print(dic['item1']) # 120

# delete
del dic['item4']
print(dic)  # item1:100, item2:200, item3:300

# key check
print('item1' in dic.keys())  # True
print('itemX' in dic.keys())  # Fals

# get keys
print(dic.keys())   # ['item1', 'item2', 'item3']

# get values
print(dic.values()) # [120, 200, 300]

# get items
print(dic.items())  # [('item1':120), ('item2':200), ('item3':300)]

