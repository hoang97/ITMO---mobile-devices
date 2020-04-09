import invoice
import matplotlib.pyplot as plt
from datetime import datetime

def frameToFloat(x):
    a = x.split()
    if len(a) == 1:
        return  float(a[0])
    else:
        b = float(a[0])
        if a[1] == 'M':
            return b*pow(2,20)
        if a[1] == 'G':
            return b*pow(2,30)

def plot_graphic(data):
    start = []
    end = []
    byte = []
    for row in data:
        string_byte = row[2]
        string_stime = row[3]
        string_etime = row[4]
        a =  string_stime.split('.')
        b =  string_etime.split('.')
        c =  frameToFloat(string_byte)
        stime = datetime.strptime(a[0],"%Y-%m-%d %H:%M:%S")
        etime = datetime.strptime(b[0],"%Y-%m-%d %H:%M:%S")
        start.append(stime)
        end.append(etime)
        byte.append(c)
    FirstStart = min(start)
    LastEnd = max(end)
    dic = {}
    for i in range((LastEnd-FirstStart).seconds+1):
        dic[i] = 0
    for i in range(len(start)):
        duration = (end[i] - start[i]).seconds + 1
        bps = byte[i]/duration
        for j in range((start[i]-FirstStart).seconds,(end[i]-FirstStart).seconds+1):
            dic[j] += bps
    y = list(dic.values())
    x = list(dic.keys())
    plt.plot(x,y)
    plt.xlabel('Duration from the 1st moment (second)')
    plt.ylabel('Byte per second')
    plt.title("User's internet usage")
    plt.show()

def show(IpNum):
    _,data = invoice.insertData(IpNum)
    plot_graphic(data)