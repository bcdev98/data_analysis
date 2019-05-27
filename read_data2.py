import csv

stocks = ['aapl', 'f']

for stk in stocks:

    myfile = open("IEX_stock_{0}_chart_1y.csv".format(stk), "r")
    reader = csv.reader(myfile)
    # get the column headers
    headers = next(reader, None)
    print(headers)

    # initialize count
    count = 0
    for x in reader:
        # columns - date, open, close, volume
        print("{0},{1},{2},{3},{4}".format(stk.upper(), x[0], x[1], x[4], x[5]))
        count = count + 1

    print("Total Data Count for {0} = {1}".format(stk.upper(), count))
    myfile.close()