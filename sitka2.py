import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file= open("sitka_weather_07-2018_simple.csv","r")

csv_file=csv.reader(open_file,delimiter=",")

header_row=next(csv_file)

print (type(header_row))

for index,column_header in enumerate(header_row):
    print(index,column_header)

highs=[]

#testing the datetime strptime function
mydate=datetime.strptime("2018-07-01","%Y-%m-%d")
print(mydate)
print(type(mydate))

dates=[]

for x in csv_file:
    highs.append(int(x[5]))
    the_date=datetime.strptime(x[2], "%Y-%m-%d")
    dates.append(the_date)

print(dates)

print(highs)


import matplotlib.pyplot as plt

#autoformat the x axis that has dates to what you think is best

fig=plt.figure()


plt.title("Daily High Temperatures, July 2018",fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)",fontsize=12)
plt.tick_params(axis="both",labelsize=12)
fig.autofmt_xdate()
plt.plot(dates, highs,c="pink")

plt.show()

