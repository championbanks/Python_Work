
"""
Author: Edwin
"""# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

import sys

py_bank_path = os.path.join('Resources', 'election_data.csv')


with open(py_bank_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Create variables to store values
    
    total = 0
    khan_count = 0
    correy_count = 0
    Li_count = 0
    O_Tooley_count = 0
    
    for row in csvreader: 
        total = total + 1
        if (row[2]) == "Khan" :
            khan_name = (row[2])
            khan_count = khan_count  + 1
        elif (row[2]) == "Correy" :
            correy_name = (row[2])
            correy_count = correy_count  + 1
        elif (row[2]) == "Li" :
            Li_name = (row[2])
            Li_count = Li_count  + 1
        elif (row[2]) == "O'Tooley" :
            O_Tooley_name = (row[2])
            O_Tooley_count = O_Tooley_count  + 1
            
# Calculate candidates percentages
Candidate_1 = round(((khan_count/total) * 100),2)
Candidate_2 = round(((correy_count/total) * 100),2)
Candidate_3 = round(((Li_count/total) * 100),2)
Candidate_4 = round(((O_Tooley_count/total) * 100),2)

# Print resuts to console
print ("Election Results",
    "----------------------------",
    f"Total votes: {total}",
    "----------------------------",
    f"{khan_name}     : {Candidate_1}% ({khan_count})",
    f"{correy_name}   : {Candidate_2}%  ({correy_count})",
    f"{Li_name}       : {Candidate_3}%  ({Li_count})",
    f"{O_Tooley_name} : {Candidate_4}%   ({O_Tooley_count})",
    "----------------------------",
    f"Winner: {khan_name}",
    "----------------------------",
    sep="\n")

# Create text file and output result 

output_file = os.path.join("Election Results.txt") 


with open(output_file , 'w') as f:
  sys.stdout = f
  
  print ("Election Results",
    "----------------------------",
    f"Total Votes: {total}",
    "----------------------------",
    f"{khan_name}     : {Candidate_1}% ({khan_count})",
    f"{correy_name}   : {Candidate_2}%  ({correy_count})",
    f"{Li_name}       : {Candidate_3}%  ({Li_count})",
    f"{O_Tooley_name} : {Candidate_4}%   ({O_Tooley_count})",
    "----------------------------",
    f" Winner: {khan_name}",
    "----------------------------",
    sep="\n")


