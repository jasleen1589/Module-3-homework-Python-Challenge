import csv

# Files to load and output (Remember to change these)
file_to_load = os.path.join("PyBank","Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_data.txt")
# Total Vote Counter
total_votes = 0
# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)

# Read the header
    header = next(reader)
    # For each row...
    print(header)






