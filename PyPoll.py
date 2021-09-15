# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize vote counters.
total_votes = 0

# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# County options and county votes.
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the county turnout, vote count, and percentage.
highest_turnout = ""
county_count = 0
county_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1
        
        #Candidate Based Data
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add to the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #County Based Data
        #Get the county name from each row.
        county_name = row[1]
        #If the county does not match any existing county, add to the county list.
        if county_name not in county_options:
            #Add the county name to the county list.
            county_options.append(county_name)
            #And begin tracking the votes from the county.
            county_votes[county_name] = 0
        #Add a vote to that county's count.
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    
    #Print Candidate Final Vote Information
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


    # After opening the file print the final vote count to the terminal.
    county_results = (
        f"\nCounty Voting Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(county_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(county_results)
    
    #Print County Final Vote Information
    for county_name in county_votes:
        # Retrieve vote count and percentage.
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > county_count) and (vote_percentage > county_percentage):
            county_count = votes
            highest_turnout = county_name
            county_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    county_summary = (
        f"-------------------------\n"
        f"County with Highest Turnout: {highest_turnout}\n"
        f"Total County Votes: {county_count:,}\n"
        f"Total County Percentage: {county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(county_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(county_summary)