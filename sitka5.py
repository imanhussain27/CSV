import matplotlib.pyplot as plt

import csv

from datetime import datetime

open_file1=open("death_valley_2018_simple.csv","r")
csv_file1=csv.reader(open_file1, delimiter= ",")
header_row1=next(csv_file1)
open_file2=open("sitka_weather_2018_simple.csv","r")
csv_file2=csv.reader(open_file2,delimiter= ",")
header_row2=next(csv_file2)

for index, column_header in enumerate (header_row1):
    print(index, column_header)

for index, column_header in enumerate (header_row2):
    print(index, column_header)

highs=[]
dates=[]
lows=[]
highs2=[]
dates2=[]
lows2=[]

for rec in csv_file1: 
    try: 
        the_date=datetime.strptime(rec[2], '%Y-%m-%d')
        high=int(rec[5])
        low=int(rec[6])
    except ValueError:
        print(f'Missing Data For {the_date}')
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(the_date)

fig=plt.figure()
plt.subplot(2,1,2)
plt.plot(dates,highs,c='red',alpha=0.3)
plt.plot(dates,lows,c='blue',alpha=0.3)
plt.title("Death Valley, CA-US")
plt.xlabel('',fontsize=8)
plt.ylabel("Temperature (F)",fontsize=8)
plt.tick_params(axis='both',which='both',labelsize=16)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
fig.autofmt_xdate()

plt.subplot(2,1,1)
plt.plot(dates2,highs2,c='red',alpha=0.3)
plt.plot(dates2,lows2,c='blue',alpha=0.3)
plt.title("Sitka Airport, AK-US")
plt.xlabel('',fontsize=8)
plt.ylabel("Temperature (F)",fontsize=8)
plt.tick_params(axis='both',which='both',labelsize=16)
plt.suptitle("Temperature Comparison Between Sitka Airport, AK-US and Death Valley, CA-US",fontsize=10)
plt.fill_between(dates2,highs2,lows2,facecolor='blue',alpha=0.1)
fig.autofmt_xdate()

plt.show()