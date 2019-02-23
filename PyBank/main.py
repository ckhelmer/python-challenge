import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline= "") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)  # skip the headers
    
    NetTotal = 0
    
    
    for row in csvreader:
        
        #Total number of months included in the dataset
        
        MonthTotal = len(row[0])
        
        #Net total of profits/losses over period
        
        NetTotal = NetTotal + int(row[1])
        
        
        #Average of changes in profits/losses over the entire period
        
        #Greatest increase in profits over the entire period
       # if row[1] == max(row[1]):
            #print("Greatest Increase in Profits: " + row[0] + max(row[1]))
    
    print("Total Months: " +  MonthTotal)        
    print("Total: " + NetTotal)            
        
        #Greatest decrease in profits over the period