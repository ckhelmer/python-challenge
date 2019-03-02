import os 
import csv

#because it's in the same file
csvpath= os.path.join("election_data.csv")

#opens the file, making each new line into a list
with open(csvpath, newline= "") as csvfile:
    
    #separates each list by commas
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)  # skip the headers
    
    candidates = []
    candidate_dictionary = {}
    percentage_dictionary = {}
    voters = 0
    winner = ""
    compare = 0
    
    for row in csvreader:
        
         
        #Total number of votes cast
        voters = voters + 1
        
        #Complete list of candidates who received votes
        #Creates a list of Candidates
        if row[2] not in candidates:
            
            candidates.append(row[2]) 
            candidate_dictionary[row[2]] = 0
            
        candidate_dictionary[row[2]] = candidate_dictionary[row[2]] + 1
    
    for candidate in candidate_dictionary:    
        
        percentage = round(((candidate_dictionary[candidate] / voters)*100),2) 
        percentage_dictionary[candidate] = percentage
        
    for candidate in candidates:
        
        if compare < percentage_dictionary[candidate]:
            compare = percentage_dictionary[candidate]
            winner = candidate
  
         
    #Print results
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(voters))
    print("---------------------------")
    print("Candidates: ")
    for candidate in candidates:
        print(candidate + ": " + str(percentage_dictionary[candidate]) + "% " + str(candidate_dictionary[candidate]))
    print("----------------------------")
    print("Winner: " + winner )    
    
    #Total Number of Votes won by each candidate
    #Percentage of votes won by each candidate
    #Winner of the election based on popular vote
filepath = os.path.join(".", "results.txt")
with open(filepath,'w') as text:
    text.write("Election Results")
    text.write("----------------------------")
    text.write("Total Votes: " + str(voters))
    text.write("---------------------------")
    text.write("Candidates: ")
    for candidate in candidates:
        text.write(candidate + ": " + str(percentage_dictionary[candidate]) + "% " + str(candidate_dictionary[candidate]))
    text.write("----------------------------")    
    text.write("Winner: " + winner )    
    
    
        