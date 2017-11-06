
with open('input/input1.csv', encoding='utf-8') as f:
    for row in f:
        columns = row.rstrip().split(',')
        print(columns)

with open('output/output.txt', 'w', encoding='utf-8') as f:
    f.write('hello world\n')
