# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code  1.60.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview
Upon review of the Election Analysis, the Election Commission has requested additional tasks to be completed regarding the election results.

1. Calculate the voter turnout for each county.
2. Calculate the percentage of votes from each county out of the total count.
3. Determine the county with the highest turnout during the election.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.60.1
 
## Challenge Summary
The additional anaylsis of the election show that:
- The election consisted of votes for the following counties:
    - Jefferson County
    - Denver County
    - Arapahoe County
- The voter turnout for each county were:
    - Jefferson County produced 10.5% of the vote with 38,855 votes.
    - Denver County produced 82.8% of the vote with 306,055 votes. 
    - Arapahoe County produced 6.7% of the vote with 24,801 votes.
- The county with the highest turnout during the election was:
    - Denver County which produced 82.8% of the vote with 306,055 votes.

## Attachments
1. [Deliverable 1.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Deliverable%201.PNG) - Screencapture of results printed to terminal.
![Deliverable 1.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Deliverable%201.PNG)
2. [Election_Analysis.txt](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/election_analysis.txt) - Election results written to a text file for delivery to the Election Commission.
3. [PyPoll_Challenge.py](https://github.com/nseddon/Election_Analysis/blob/main/PyPoll_Challenge.py) - Source code for the analysis

## Election Audit Summary
The code currently provides a summary for state based elections with the ability to present:
1. Statewide Metrics
    - Total votes received during the election.
    - Declaration of winning Candidate, including vote count and percentage of the total vote.
2. County Based Metrics
    - Names of counties where at least one vote was cast.
    - Total votes received within each county
    - Percentage of the Statewide Total Vote received within each County
    - Name of County with the highest voter turnout.
3. Candidate Based Metrics
    - Names of candidates that received at least one vote.
    - Total votes received by each candidate.
    - Percentage of the Statewide Total Vote received by each candidate.

Additional results from analysis may be obtained through code and data modification:
1. Statewide Metrics
    - Percentage of population that voted in the election
          - Inclusion of all ballots issued, even if not cast, in the csv would be required.
          - Code manipulation would require how total votes are calculated to be modified
          - Code manipulation would require an additional tracker to count the number of ballots issued.
[Modification 1-1.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%201-1.PNG) - Original Code for total votes counted.
![Modification 1-1.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%201-1.PNG)
    

