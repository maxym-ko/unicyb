import csv

with open('good.csv', encoding='cp1251') as f:
    it = csv.reader(f, delimiter=';')
    data = []
    for row in it:
        if row:
            data.append(row)
header = data[0].copy()
data = data[1:]

print(header, data)
