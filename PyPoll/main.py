import os
import csv

# Set path for file
csv_path = os.path.join("PyPoll","Resources","election_data.csv")

#Set up the lists to store the months and profits
unique_candidates = []
votes = []
percentages = []

# Open the CSV using the UTF-8 encoding
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # Add data in the months column to the months list
        votes.append(row[2])

#Close the file
csvfile.close()

#Looping through the votes list:
for i in votes:
    #if the candidate is not in the unique_candidates list
    if i not in unique_candidates:
        # add the candidate to the list
        unique_candidates.append(i)
    #Initialize list for counting votes for each candidate
    vote_count = []

#find the total number of votes for each candidate
for i in unique_candidates:
    # add the number of votes for each candidate to the votes list
    percentages.append(votes.count(i))

#Loop through the list with the unique candidates
for i in unique_candidates:
    #Loop through the votes with all candidates
    for j in votes:
        #if the candidate in the unique candidates list matches the candidate in the votes list
        if i == j:
            # add the candidate to the vote count list
            vote_count.append(i)
            #increment count to count in the unique candidates list
            count = (round ((len(vote_count)/len(votes))*100,3))
#Set count to zero to start counting the votes for the next candidate
count = 0

# count the total votes
total_votes = len(votes)
# create a dictionary with the candidates and their vote counts  
candidate_votes = dict(zip(unique_candidates, percentages))
voting_results = dict(zip(unique_candidates, percentages))
# determine the winner by getting the key of the candidate with the maximum value
winner = max(candidate_votes, key=candidate_votes.get)

#Specify the file to write to
output_path = os.path.join("PyPoll","analysis","results.txt")
#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    #Write the content on to a text file
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------\n") 
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("----------------------------\n")

    # Write each candidate's in the dictionary along with their percentage of votes and their vote counts on to the text file
    for key in voting_results:
        txtfile.write(key + ": " + str(round((voting_results[key]/total_votes)*100,3)) + "% (" + str(voting_results[key]) + ")\n")

    txtfile.write("----------------------------\n")
    txtfile.write("Winner: " + winner + "\n")


#Open the output file in read mode
with open(output_path, 'r') as txtfile:

    #Print the contents of the text file
    print(txtfile.read())

    #Close the file
    txtfile.close()
    

