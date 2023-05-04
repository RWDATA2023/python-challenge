import csv
import os
# Set up variables to store results
total_votes = 0
candidate_votes = {}
winner = {"name": "", "votes": 0}

# Open CSV file and read contents
election_data_csv = os.path.join("Resources", "election_data.csv")
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip header row
    next(csv_reader)
    for row in csv_reader:
        # Update total number of votes
        total_votes += 1
        # Add candidate to dictionary if not already present
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 0
        # Increment candidate's vote count
        candidate_votes[row[2]] += 1

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    # Calculate percentage of votes
    vote_percentage = votes / total_votes * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    # Update winner if necessary
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Export results to text file
with open("election_results.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        # Calculate percentage of votes
        vote_percentage = votes / total_votes * 100
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner['name']}\n")
    txt_file.write("-------------------------\n")

print("Results exported to election_results.txt")
