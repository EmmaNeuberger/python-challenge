# Import dependencies
import os
import csv

# Set path
poll_path = os.path.join('election_data.csv')

# Set variables and lists
total_votes = 0
correy = 0
khan = 0
li = 0
otooley = 0

# Open csv 
with open(poll_path, newline="") as csvfile:
    poll_reader = csv.reader(csvfile, delimiter=",")

    header = next(poll_reader)
    # Identify header and skip
    print(f"Header: {header}")    

    # Iterate through each row in the csv
    for row in poll_reader: 

        # Total votes
        total_votes = total_votes +1

        # Count votes for each candidate
        if row[2] == "Correy": 
            correy = correy + 1
        elif row[2] == "Khan":
            khan = khan + 1
        elif row[2] == "Li": 
            li = li + 1
        elif row[2] == "O'Tooley":
            otooley = otooley + 1

 # Create lists that correspond to candidate and vote count
candidates = ["Correy", "Khan", "Li", "O'Tooley"]
votes = [correy, khan, li, otooley]

# Combine candidates and votes
zip_lists = dict(zip(candidates,votes))

# Winner
winner_key = max(zip_lists, key=zip_lists.get)

correy_percent = (correy/total_votes) * 100
khan_percent = (khan/total_votes) *100
li_percent = (li/total_votes)* 100
otooley_percent = (otooley/total_votes) * 100

# Print to terminal
print(f"Election Results")
print(f"----------------------------------")
print(f"Winner: {winner_key}")
print(f"----------------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------------")
print(f"Correy: [{correy}] {correy_percent:.3f}%")
print(f"Khan: [{khan}] {khan_percent:.3f}%")
print(f"Li: [{li}] {li_percent:.3f}%")
print(f"O'Tooley: [{otooley}] {otooley_percent:.3f}%")
print(f"----------------------------------")

# Output csv
output_file = os.path.join('election_results.csv')

with open(output_file,"w") as file:

    # Write to csv
    file.write(f"Election Results \n")
    file.write(f"---------------------------------- \n")
    file.write(f"Winner: {winner_key} \n")
    file.write(f"---------------------------------- \n")
    file.write(f"Total Votes: {total_votes} \n")
    file.write(f"---------------------------------- \n")
    file.write(f"Correy: [{correy}] {correy_percent:.3f}% \n")
    file.write(f"Khan: [{khan}] {khan_percent:.3f}% \n")
    file.write(f"Li: [{li}] {li_percent:.3f}% \n")
    file.write(f"O'Tooley: [{otooley}] {otooley_percent:.3f}% \n")
    file.write(f"---------------------------------- \n")