
Hessari

import os
import csv

my_input_file = '/Users/hessari/Desktop/Budget/budget_data.csv'

TotalMonths = 0
highest = 0
lowest = 100000000000000
totalsum = 0
averagemonth = 0
rowcount = 0
i = 0
previous = 0
current = 0
running = 0


with open(my_input_file, newline="") as csv_file:
        csvreader = csv.reader(csv_file, delimiter=",")   
        next(csvreader, None)
    
        for row in csvreader:
        
            if int(row[1]) >= highest:
                highest = int(row[1])
                highname = str(row[0])

            if int(row[1])	 <= lowest:
                lowest = int(row[1])
                lowname = str(row[0])
TotalMonths = TotalMonths + 1           
totalsum = int(totalsum) + int(row[1])
rowcount = rowcount + 1

while i <= rowcount-2:
        previous = current
        current = int(row[1])
        running = running + (current - previous)
        i = i + 1
        
        averagemonth = running / rowcount
        
print("Financial Analysis")
print("------------------------")
print("TotalMonths: " + str(rowcount))
print("Total Revenue: $" + str(totalsum))
print("Average Revenue Change: $" + str(round(averagemonth,2)))
print("Greatest Increase in Revenue: $" + str(highest) + " on " + highname)
print("Greatest Decreased in Revenue: $" + str(lowest) + " on " + lowname)


Financial Analysis
------------------------
TotalMonths: 3
Total Revenue: $2013297
Average Revenue Change: $223699.67
Greatest Increase in Revenue: $1170593 on Feb-2012
Greatest Decreased in Revenue: $-1196225 on Sep-2013

#reader
