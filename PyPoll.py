# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who receieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

#Add our dependencies
import os
import csv

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Array to generate the full list of candidates
candidate_options = []

#Dictionary for counting the votes for each candidate
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winnig_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

	#To do: read and analyze the data here
	file_reader = csv.reader(election_data)

	#Print the header row.
	headers = next(file_reader)

	#Print each row in the CSV file.
	for row in file_reader:
		#Add to the total vote count.
		total_votes += 1
		#Print the candidate name from each row
		candidate_name = row[2]

		#"candidate_name1": votes, "candidate_name2": votes, "candidate_name3": votes

		#If the candidate does not match any existing candidate...
		if candidate_name not in candidate_options:
			#Add the candidate_name to the candidate_options list
			candidate_options.append(candidate_name)

			#Tracker for each of the candidate's vote count
			candidate_votes[candidate_name] = 0

		#Add a vote to that candidate's count.
		candidate_votes[candidate_name] += 1	

#Determine the percentage of votes for each candidate by looping through the counts.
#Iterate through the candidate list.
for candidate_name in candidate_votes:
	#Retrieve vote count of a candidate.
	votes = candidate_votes[candidate_name]
	#Calculate the percentage of votes.
	vote_percentage = float(votes)/float(total_votes) * 100
	#Print the candidate name and percentage of votes.
	print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
	
	#Determine winning vote count and candidate
	#Determine is the votes are greater than the winning count.
	if (votes > winning_count) and (vote_percentage > winning_percentage):
		#If true then set winning_count = votes and winning_percentage = vote_percentage
		winning_count = votes
		winning_percentage = vote_percentage
		#Set the winning_candidate equal to the candidate's name.
		winnig_candidate = candidate_name
	winning_candidate_summary = (
		f"-------------------------\n"
		f"Winner: {winnig_candidate}\n"
		f"Winning Vote Count: {winning_count:,}\n"
		f"Winning Percentage: {winning_percentage:.1f}%\n"
		f"-------------------------\n")
print(winning_candidate_summary)
	


#Print the candidate vote dictionary
#print(candidate_votes)

#Print the candidate list.
#print(candidate_options)

#Print the total votes.
#print(total_votes)

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

	# Add a header to the write file.
	txt_file.write("Counties in the Election\n_________________________\n")
	
	# Write three counties to the file.
	txt_file.write("Arapahoe\nDenver\nJefferson")

#Close the file
election_data.close()




