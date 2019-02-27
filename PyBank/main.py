import os
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline= "") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)  # skip the headers
    
    NetTotal = 0
    MonthlyChange = 0
    AverageChange = 0
    Change = 0
    RunningChange = 0
    MonthTotal = 0
    months = []
    revenue = []
    dictionary = {}
    
    
    #define dictionary HERE
    
    for row in csvreader:
      
        #make row[1] into an int
        row[1]= int(row[1])
        
        #create list to store months revenu
        months.append(row[0])
        revenue.append(row[1])
              
        #add dictionary reference month by amount
        dictionary[row[1]] = row[0]
        
        #Total number of months included in the dataset
        
        MonthTotal = MonthTotal + 1                
             
        #Net total of profits/losses over period
        
        NetTotal = NetTotal + row[1]
        
        
    
        
    #Average of changes
    #First subtract one value from the next over the course of the revenue list
    MonthlyChange = [x-y for x, y in zip(revenue, revenue[1:])] 
    #Add the changes together and divide by total of changes (months-1). Round final answer.
    AverageChange = round(sum(MonthlyChange)/(MonthTotal-1),2 )
       
    
    #Maximum Value
    maximum = max(revenue)
    maximumdate = (dictionary[maximum])
        
    #minimum Value
    minimum = min(revenue)
    minimumdate = (dictionary[minimum])
    
   
    #print all statements OUTSIDE LOOP
    
    print("Financial Analysis")
    
    print("----------------------------------")
    
    print( "Total Months in Period: " + str(MonthTotal))
    print("Total Revenue: $" + str(NetTotal))
    print("Average Monthly Change: $" + str(AverageChange)) 
    print("Greatest Decrease in Profits: " + minimumdate + " $ " + str(minimum))
    print("Greatest Increase in Proftis: " + maximumdate + " $ " + str(maximum))
    
   #write results to text file
   

filepath = os.path.join(".", "results.txt")
with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    
    text.write("----------------------------------" + "\n")
    
    text.write( "Total Months: " + str(MonthTotal) + "\n")
    text.write("Total Revenue: $" + str(NetTotal) + "\n")
    text.write("Average Monthly Change: $" + str(AverageChange) + "\n") 
    text.write("Greatest Decrease in Profits: " + minimumdate + " $ " + str(minimum) + "\n")
    text.write("Greatest Increase in Proftis: " + maximumdate + " $ " + str(maximum) + "\n")
    
    