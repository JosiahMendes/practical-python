# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    totalCost = 0.0
    try:
        f = open(filename, 'rt')
    except FileNotFoundError:
        print("File not found", filename)
    headers = next(f)
    for line in f:
        row = line.split(',')
        try:
            totalCost = totalCost + int(row[1])*float(row[2])
        except ValueError:
            print("Missing data, skipping row ",line)
    f.close()
    return totalCost

cost = portfolio_cost('Data/portfolio.csv')
print('Total Cost is ',cost)
