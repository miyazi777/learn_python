list = [111, 222, 333]

# access
print(list) # [111, 222, 333]
print(list[0])  # 111
print(list[2])  # 333

# add
list.append(444)
print(list) # [111, 222, 333, 444]

list.insert(1, 555)
print(list) # [111, 555, 222, 333, 444]

# update
list[0] = 666
print(list) # [666, 555, 222, 333, 444]

# delete
list.pop(0)
print(list) # [555, 222, 333, 444]
list.pop(-1)
print(list) # [555, 222, 333]

# length
print(len(list))    # 3

# loop
for x in list:
    print(x)
