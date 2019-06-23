# Import dependencies
import os
import csv
from collections import Counter

# Declaration of variables
voter = []
country = []
candidate = []

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

def total_votes(voter):
	return len(voter)

def percentages(candidate):
    # Convert list of candidates into dictionary
    # output will be likes candidate {'A':2, 'B':4}
    votes = Counter(candidate)

    candidates = []
    num_votes = []

    #takes dictionary keys and values and, respectively, dumps them into the lists, 
    # candidates and num_votes
    for key, value in votes.items():
        candidates.append(key)
        num_votes.append(value)

    # creates vote percent list
    vote_percent = []
    for i in num_votes:
        vote_percent.append(int(round(i/len(candidate)*100, 1)))

    # zips candidates, vote_percent, num_votes into tuples
    percent_data = list(zip(candidates, vote_percent, num_votes))

    return percent_data

def winner(candidate):
    # Convert list of candidates into dictionary
    # output will be likes candidate {'A':2, 'B':4}
    votes = Counter(candidate)

    # Create another dictionary and it's key will
    # be count of votes values will be name of
    # candidates
    dict = {}

    for value in votes.values():
        # Initialize empty list to each key to
        # insert candidate names having same
        # number of votes
        dict[value] = []

    for (key, value) in votes.items():
        dict[value].append(key)

    # Sort keys in descending order to get maximum
    # value of votes    
    maxVote = sorted(dict.keys(), reverse = True)[0]

    # Check if more than 1 candidates have same
    # number of votes. If yes, then sort the list
    # first and print first element
    if len(dict[maxVote]) > 1:
        return (sorted(dict[maxVote])[0])
    else:
        return (dict[maxVote][0])

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
    	voter.append(row[0])
    	country.append(row[1])
    	candidate.append(row[2]) 

    print("Election Results")
    print("-------------------------")
    print("Total votes: " + str(total_votes(voter)))
    print("-------------------------")
    for per in percentages(candidate):
        print(str(per[0]) + ": " + str(per[1]) +'% (' + str(per[2]) + ')')
    print("-------------------------")
    print("Winner: " + winner(candidate))
    print("-------------------------")

# Set variable for output file
output_file = os.path.join("election_results.txt")

# Open the output file
with open(output_file,'w') as text:
    text.write("Election Results" + "\n")
    text.write("-------------------------" + "\n")
    text.write("Total votes: " + str(total_votes(voter)) + "\n")
    text.write("-------------------------" + "\n")
    for per in percentages(candidate):
        text.write(str(per[0]) + ": " + str(per[1]) +'% (' + str(per[2]) + ')'+ "\n")
    text.write("-------------------------" + "\n")
    text.write("Winner: " + winner(candidate) + "\n")
    text.write("-------------------------" + "\n")