# # Import dependencies
# import os
# import csv

# # Create path
# poll_path = os.path.join(".", "election_data.csv")

# total_votes = []
# candidate = {}

# # Open
# with open(poll_path, newline="") as csvfile:
#     # Read
#     poll_reader = csv.reader(csvfile, delimiter=",")

#     print(poll_reader)

#     head = next(poll_reader)
#     print(f"Head: {head}")

#     for row in poll_reader:
#         total_votes.append(row[0])

#         candidate.append(row[2])


#     print(len(total_votes))
#     print(candidate.keys())


import csv
import os


#comment
# Set path for file
csvpath = os.path.join(".", "election_data.csv")
file_to_ouput = "analysis/election_analysis.txt"
# file_to_load = "raw_data/election_data.csv"

#print(csvpath)

# Open and read the CSV
with open(csvpath) as csvfile:
    #print(csvreader)
    
    # Read header row, print it, set it aside
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
 
    #
    Candidates = {}
    Count = 0
    Votes_Cast = 0
    percent_of_votes = 0
    Most_Votes = 0
    Most_Voted = ""
    

    
    for row in csvreader:
        
        # Count the total number of votes cast
        candidate = row[2]
        Count += 1
        if candidate in Candidates.keys():
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1
        #print(Candidates)
    
    
    # Print Statements
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {Count}")
    print("-------------------------------")
    
            
    #total number of votes for each candidate
    for candidate in Candidates:
        Votes_Cast += Candidates[candidate]
    
        # percent of votes for each candidate
        percent_of_votes = (Candidates[candidate])/(Count) * 100
        print(f"{candidate}: {int(percent_of_votes)}% {Votes_Cast}")
        
        if Candidates[candidate] > Most_Votes:
            Most_Voted = candidate
            Most_Votes = Candidates[candidate]
        
        
    
    # The winner of the election based on popular vote.
    print("-------------------------------")
    
    print(f"Winner: {Most_Voted}")
    
    print("-------------------------------")



#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------