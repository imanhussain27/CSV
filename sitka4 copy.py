import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file= open("death_valley_2018_simple.csv","r")

csv_file=csv.reader(open_file,delimiter=",")

header_row=next(csv_file)

print (type(header_row))

for index,column_header in enumerate(header_row):
    print(index,column_header)


highs=[]

lows=[]

#testing the datetime strptime function
mydate=datetime.strptime("2018-07-01","%Y-%m-%d")
print(mydate)
print(type(mydate))

dates=[]

for x in csv_file:
    try:
        high = int(x[4])
        low = int(x[5])
        the_date=datetime.strptime(x[2], "%Y-%m-%d")

    except ValueError:
        print(f"missing data for {the_date}") 
    else: 
        highs.append(high)
        lows.append(low)
        dates.append(the_date)

#print(dates)

#print(highs)

#print(lows)

import matplotlib.pyplot as plt

#autoformat the x axis that has dates to what you think is best

fig=plt.figure()


plt.title("Daily high and low temperatures- 2018\nDeath Valley",fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis="both",labelsize=12)
fig.autofmt_xdate()
plt.plot(dates, highs,c="pink",alpha=0.5)
plt.plot(dates,lows, c="purple",alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor="blue",alpha=0.1)

plt.show()

#for subplot, the first argument is the number of rows, then columns, then it's index

plt.subplot(2,1,1)
plt.plot(dates,highs,c="green")
plt.title("Highs")

plt.subplot(2,1,2) 
plt.plot(dates,lows,c="purple")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()
