# Add our dependencies.
import csv
import os
# Add a variable to load a file from a path.
#file_to_load = os.path.join("../PyPoll/Resources/election_data.csv")
csv_file = os.path.join("../PyPoll/Resources/election_data.csv")

# Open the election results and read the file
# A list to capture the names of candidates
candidates = []

# List the number of votes 
num_votes = []

# Percentage of total votes per candidade
percent_votes = []

# Count of number of votes 
total_votes = 0
#with open(file_to_load) as election_data:
    #file_reader = csv.reader(election_data)
    # Read header row.
    #headers = (next(file_reader))
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
with open(csv_file, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to our vote-counter 
        total_votes += 1 

        '''
        If the candidate is not on our list, add his/her name to our list, along with 
        a vote in his/her name.
        If he/she is already on our list, we will simply add a vote in his/her
        name 
        '''
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.1f%%" % percentage
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
#output.write('{}\n{}\n{}\n'.format(line5, line6, line7)) python main.py