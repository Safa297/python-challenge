import os
import csv

# Set the path to the CSV file
csv_path = os.path.join("PyPoll", "Resources", "election_data.csv")

# Initialize variables to store analysis results
total_votes = 0
candidate_votes = {}

# Read the CSV file and process the data
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        # Check if the candidate is already in the dictionary, and if not, add them
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Prepare the analysis report
results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

for candidate, votes in candidate_votes.items():
    results += f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n"

results += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
output_file = os.path.join("PyPoll", "Analysis", "election_results.txt")
with open(output_file, "w") as textfile:
    textfile.write(results)
