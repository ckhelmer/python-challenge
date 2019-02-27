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
    VoteCounts = []
    voters = 0
    candidatecount = 0
    candidate_dictionary = {}
    
    for row in csvreader:
        
        #Total number of votes cast
        voters = voters + 1
        
        #Complete list of candidates who received votes
        #Creates a list of Candidates
        if row[2] not in candidates:
            candidates.append(row[2])    

    #OUTSIDE LOOP, create candidate dictionary
    
     
    for candidate in candidates:
        
        candidate_dictionary = {candidate : 0}
    
        
        #WHY DOES THIS WORK IN THE FOR LOOP BUT NOT OUTSIDE OF IT?
        print(candidate_dictionary)
    
    for row in csvreader:
                
            if candidate == row[2]:
                
                        
        #Total number of votes won by each candidate
        
        #Winner of the election based on popular vote
        
        
    #Print results
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(Voters))
    print("---------------------------")
    
    #Total Number of Votes won by each candidate
    #Percentage of votes won by each candidate
    #Winner of the election based on popular vote
    
    
    for candidate in Candidates:
        print(str(candidate) , str(candidatecount))
    
        