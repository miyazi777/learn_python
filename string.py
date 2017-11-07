# 分割
str = 'a,b,c'
ary = str.split(',')
print(ary)  # ['a', 'b', 'c']

# 置換
str = 'abcde'
str2 = str.replace('de', 'ab')
print(str2) # abcab

str = 'ab ab ab'
str2 = str.replace('ab', 'cd', 2)
print(str2) # cd cd ab

# format
print('xxx {} xxx {}'.format('111', '222')) # xxx 111 xxx 222
print('xxx {0} xxx {1}'.format('111', '222')) # xxx 111 xxx 222
print('xxx {str1} xxx {str2}'.format(str1='111', str2='222')) # xxx 111 xxx 222
