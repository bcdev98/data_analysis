import csv
import sqlite3

myList = []
for s in ['F', 'MSFT']:
    myfile = open("IEX_stock_{0}_chart_1y.csv".format(stk), "r")
    reader = csv.reader(myfile)
    # get the column headers
    headers = next(reader, None)
    print(headers)

    for x in reader:
        # columns - stk, date, open, high, low, close, volume
        tup = ({0},{1},{2},{3},{4},{5},{6})
        myList.append(tup)
    myfile.close()

print("Total Data List = {0}".format(len(myList)))

conn = sqlite3.connect("/Users/bcui/devops/proj/data_analysis/db/stocks.db")
c = conn.cursor()
c.executemany('Insert into stockprices values(?,?,?,?,?,?,?)', myList)
conn.commit()
conn.close()
print("Total Row Saved = {0}".format(c.rowcount))