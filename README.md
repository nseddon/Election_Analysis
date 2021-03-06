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
### The code currently provides a summary for state based elections with the ability to present:
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

### Additional results from analysis may be obtained through code and data modification:
1. Country Based Metrics
    - Additional sections of code could be inserted to track overall state data to allow for the program to be used in national elections.

2. State Based Metrics
    - Percentage of population that voted in the election.
        - Inclusion of all ballots issued, even if not cast, in the csv would be required.
        - Code manipulation would require modifciation of how total votes are calculated.
        - Code manipulation would require an additional tracker to count the number of ballots issued.
        - [Modification 1-1.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%201-1.PNG) - Original Code for total votes counted.![Modification 1-1.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%201-1.PNG)
        - [Modification 1-2.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%201-2.PNG) - Modified Code for total votes counted and ballots issued.![Modification 1-2.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%201-2.PNG)
    
3. County Based Metrics
    - Percentage of county population that voted in the election.
        - No further csv adjustments necessary if the statewide adjustment has been made.
        - Code manipulation would require modification of how total votes are calculated in the county.
        - Code manipulation would require an additional tracker to count the number of ballots issued within the county.
        - [Modification 2-1.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%202-1.PNG) - Original Code for total votes counted.![Modification 2-1.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%202-1.PNG)
        - [Modification 2-2.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%202-2.PNG) - Modified Code for total votes counted and ballots issued.![Modification 2-2.png](https://github.com/nseddon/Election_Analysis/blob/main/Analysis/Modification%202-2.PNG) 

4. Candidate Based Metrics
    - True Percentage of population that voted for each candidate.
        - No further csv adjustments necessary if the statewide adjustment has been made.
        - Code addition would allow for percentage of vote received from total ballots in addition to ballots cast.

5. Further demographic information could be analyzed.
    - Inclusion in .csv file of age, education, party affiliation, lists of issues candidate intends to address, etc. would allow for additional studies to be concluded.

6. Use of existing code with terminology modification for other analyses
    - Modification of the variable names would allow existing code to track other election results.  For example, rather than a county and candidate name, an individual county could adjust this code to count up votes for a specific measure, such as budgetary increases for the school system.  
        - Adjust the county name for the bill/amendment name to track votes for each measure.
        - Adjust the candidate name to track if the vote cast was for or against the measure.
        - .csv data would include the ballot number, name of the measure, and vote cast as the three lines of data.
        - Additional adjustment would be required in the printing sections of code to ensure proper presentation of the voting analysis on the bills.
  
### Future Use Summary
With some or all of the modifications to the .csv data file suggested above, future analysis could provided data to assist with the following:

1. How to increase overall voter turnout
2. How to increase demographic based voter registration and turnout.
3. Redrawing of voter district lines to further improve fairness in the election systems based on population changes.
4. Analysis of voter concerns that dictated their vote.
5. Measure/Issue specific voting counts for additional presentation.
         
    
