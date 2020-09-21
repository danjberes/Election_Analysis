# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Declare candidate list
candidate_options = []

#Declare empty dictionary to assign votes to a candidate
candidate_votes = {}

#Winning Candidate Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    #Print each row to the .csv file and add to total vote count
    for row in file_reader:
        total_votes += 1

        #Print the candidate name from each row
        candidate_name =row[2]
        
        #Add candidates to list if their name is unique
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Track candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to candidate
        candidate_votes[candidate_name] += 1

#Calculate the percentage of votes for each candidate
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100

    #If statement to assign winner to previously stated variables
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    #Print candidate's name, votes, and percentage of vote
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)

# Close the file
election_data.close()
