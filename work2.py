#Import os and csv
import os
import csv

csvpath = os.path.join("election_data.csv")

# Total Vote Counter
total_votes = 0

# Candidate Options and Vote Counters
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
   
    # Skip the header
    header = next(reader)

    # For each row add the total vote count
    for row in reader:
        
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_names = row[2]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_names not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_names)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_names] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_names] = candidate_votes[candidate_names] + 1
        # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

    print("Election Results")
    print("-------------------------")
    print("Total Votes", total_votes)
    print("-------------------------")
    print(candidate_options, (vote_percentage), (votes))
    print("-------------------------")
    print("Winner: ", winning_candidate)
    