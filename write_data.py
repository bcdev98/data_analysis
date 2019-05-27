import csv
#
# 1. open a file called myData.csv for write
# 2. the a list of stocks and read the stock input file
# 3. read the file and write out the data to the myData.csv
# 4. close out the file
#

with open("myData.csv", "w") as f:
    stocks = ['aapl', 'f']
    for stk in stocks:
        myfile = open("IEX_stock_{0}_chart_1y.csv".format(stk), "r")
        reader = csv.reader(myfile)
        # get the column headers
        headers = next(reader, None)
        count = 0

        for x in reader:
            f.write("{0},{1},{2},{3},{4}\n".format(stk.upper(), x[0], x[1], x[4], x[5]))
            count = count + 1
        print("Total Count for {0} is {1}".format(stk.upper(), count))
        myfile.close()
print("Task is Done")
            