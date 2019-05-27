import csv

def getStockDict():
    datafile = "companylist.csv"
    f = open(datafile, "r")
    reader = csv.reader(f)
    # create an empty dictionary
    myDict = {}
    for data in reader:
        myDict[data[0]] = data[1]
    # return the dictionary
    return myDict

myDict = getStockDict()
myStocks = ['FB', 'GOOG', 'AAPL']

for x in myStocks:
    if x in myDict:
        print ("Name of {0} is {1}".format(x, myDict[x]))
