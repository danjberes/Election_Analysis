# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has asked the following tasks to be completed for the election audit of a recent congressional election.

1. Calculate total number of votes cast
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
-Data Acquired from: [election_results.csv](https://github.com/danjberes/Election_Analysis/blob/master/Resources/election_results.csv)

-Software: Python v.3.8.5, Visual Studio Code v.1.49.1

## Election Audit Results
The analysis run of the election determines that
-Total Votes: 369,711
-The follow Counties Submitted: Percentage of votes (number of votes):
  Jefferson: 10.5% (38,855)
  Denver: 82.8% (306,055)
  Arapahoe: 6.7% (24,801)
-The county with the highest turnout was Denver county with 82.8% of the vote submitted coming from that county with a total of 306,055 votes.
-The Following Candidates Received: Percentage of votes (number of votes):
  Charles Casper Stockham: 23.0% (85,213)
  Diana DeGette: 73.8% (272,892)
  Raymon Anthony Doane: 3.1% (11,606)
-The winner of the election was Diana DeGette who receieved 73.8% of the vote and 272,892 total votes.

## Election Audit Summary
Granted the results can be moved into a .csv file, this code can be adapted to audit other elections. The changes that would need to be made would be lines 5,7 to adapt to the file path and potentially 44, and 57 if the row data are switched. If this code was to be used for national elections, the county code could be adapted to state code, or for more local elections countys could be changed to districts.
