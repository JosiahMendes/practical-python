# pcost.py
#
# Exercise 1.27
totalCost = 0.0

f = open('Data/portfolio.csv', 'rt')
headers = next(f)
for line in f:
    row = line.split(',')
    totalCost = totalCost + int(row[1])*float(row[2])

f.close()
print('Total Cost is ',totalCost)
