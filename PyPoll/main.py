# allows to create paths across operating systems
import os

# allows us to import our .csv file
import csv

# setting the paths for both the .csv and the output .txt files
pybank_dir = os.path.dirname(__file__)
csvpath = os.path.join(pybank_dir, "resources/election_data.csv")
csvoutput = os.path.join(pybank_dir, "analysis/election_output.txt")

# three lists for capturing votes and a counter for the total number of votes
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

# opening the .csv and how to read it
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    # for every row in 'csvreader'...
    for row in csvreader:
        
        # count total votes
        total_votes += 1 

        # if the candidate is not in the list...
        if row[2] not in candidates:

            # add their name to the list, add their votes
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)

        # if they're already in the list...
        else:

            # just add the vote
            index = candidates.index(row[2])
            num_votes[index] += 1
    

    # add percentages to list
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    # Finding the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]


# Exporting to .txt file
output = open(csvoutput, "w")

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

output.write('{}\n{}\n{}\n'.format(line5, line6, line7))