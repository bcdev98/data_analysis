import csv

myfile = open("IEX_stock_aapl_chart_1y.csv", "r")
reader = csv.reader(myfile)
# get the column headers
headers = next(reader, None)
print(headers)

# initialize count
count = 0
for x in reader:
    # columns - date, open, close, volume
    print("{0},{1},{2},{3}".format(x[0], x[1], x[4], x[5]))
    count = count + 1

print("Total Data Count = {0}".format(count))
myfile.close()