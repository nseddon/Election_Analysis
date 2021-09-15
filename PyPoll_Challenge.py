# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
# County options and county votes.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
# Track the county turnout, vote count, and percentage.
highest_turnout = ""
county_count = 0
county_percentage = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        #Get the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        #If the county does not match any existing county, add to the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            #Add the county name to the county list.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            #And begin tracking the votes from the county.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        #Add a vote to that county's count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    #Print County Final Vote Information
    for county_name in county_votes:
        
        # 6b: Retrieve the county vote count.
        # Retrieve vote count and percentage.
        votes = county_votes[county_name]
            
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # 6d: Print the county results to the terminal.
        # Print each county's voter count and percentage to the terminal.
        print(county_results)

        # 6e: Save the county votes to a text file.
        #  Save the candidate results to our text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > county_count) and (vote_percentage > county_percentage):
            county_count = votes
            highest_turnout = county_name
            county_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    # Print the winning candidate's results to the terminal.
    county_summary = (
        f"-------------------------\n"
        f"County with Highest Turnout: {highest_turnout}\n"
        f"Total County Votes: {county_count:,}\n"
        f"Total County Percentage: {county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(county_summary)

    # 8: Save the county with the largest turnout to a text file.
    # Save the winning candidate's results to the text file.
    txt_file.write(county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
