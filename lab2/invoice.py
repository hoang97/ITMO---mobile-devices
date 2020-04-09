import csv

dataFile = 'data1.txt'

def insertData(IpNum):
    fiels = []
    rows = []
    with open(dataFile,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fiels = csvreader.__next__()
        for row in csvreader:
            rows.append(row)
    res = []
    for row in rows:
        string = row[0].split()[0]
        if string == IpNum:
            res.append(row)
    return fiels,res