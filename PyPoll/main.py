# Add our dependencies.
import csv
import os
# Add a variable to load a file from a path.
#file_to_load = os.path.join("../PyPoll/Resources/election_data.csv")
csv_file = os.path.join("../PyPoll/Resources/election_data.csv")

# Open the election results and read the file
# A list to capture the names of candidates
candidates = []
tracking_votes = {}
# List the number of votes 
num_votes = []

# Percentage of total votes per candidade
percent_votes = []

# Count of number of votes 
total_votes = 0
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
            #adding a candidate to a candidate arry if it is not there
            candidates.append (row[2])
            #initialize a candidate in the dictionnary with 0 votes 
            tracking_votes [row[2]] = 0
        else:
            tracking_votes[row[2]] += 1

    
    # Add to percent_votes list 
    # for key in tracking_votes:
    #     percentage = (tracking_votes[key]/total_votes) * 100
    #     percentage = round(percentage)
    #     percentage = "%.1f%%" % percentage
    #     percent_votes.append(percentage)
    
    # Find the winning candidate
    # winner = max(num_votes)
    # index = num_votes.index(winner)
    # winning_candidate = candidates[index]

# Displaying results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for key in tracking_votes:
    print(f"{key}: {(tracking_votes[key]/total_votes):.2%} ({str(tracking_votes[key])})") 
print("--------------------------")
index_dictionnary = 0
winner = ""
for key in   tracking_votes:
    if index_dictionnary == 0:
        max_votes = tracking_votes[key]
        index_dictionnary += 1
        winner = key
    else:
        index_dictionnary += 1
        if tracking_votes[key] > max_votes:
            max_votes = tracking_votes[key]
            winner = key
            
print(f"Winner: {winner}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for key in tracking_votes:
    line = (f"{key}: {(tracking_votes[key]/total_votes):.2%} ({str(tracking_votes[key])})") 
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7)) 