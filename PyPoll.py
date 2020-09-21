#Add dependencies.
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
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

#Declare county list and votes
county_options = []
county_votes = {}

#Winning county tracker
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row.
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

        #Print the county name from each row
        county_name =row[1]
        
        #Add county to list if their name is unique
        if county_name not in county_options:
            county_options.append(county_name)

            #Track county's vote count
            county_votes[county_name] = 0

        #Add a vote to a county
        county_votes[county_name] += 1

#Save the results to text file.
with open(file_to_save, "w") as txt_file:

    #Print final vote count into txt document
    election_results = (
        f"Election Results\n"
        f"---------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    #Calculate the percentage of votes from each county
    for county_name in county_votes:
        votes = county_votes[county_name]
        county_vote_percentage = float(votes) / float(total_votes) * 100

        #Assign winning county
        if (votes > winning_county_count) and (county_vote_percentage > winning_county_percentage):
            winning_county_count = votes
            winning_county_percentage = county_vote_percentage
            winning_county = county_name
            
        #Print county results
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
    
    #Print winning county into txt file
    winning_county_summary = (
        f"\n---------------------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"---------------------------------------\n\n")
    print(winning_county_summary)
    txt_file.write(winning_county_summary)

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
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n\n")
        print(candidate_results)
        #Print results into txt file
        txt_file.write(candidate_results)
            
    winning_candidate_summary = (
        f"---------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------------\n")
    #Print winning candidate into txt file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)