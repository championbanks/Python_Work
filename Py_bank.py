

#Author: Edwin 
# First we'll import the os module and create file paths.
import os

# Module for reading CSV files and using operating system
import csv
import numpy as np
import sys

# Collect budget data
py_bank_path = os.path.join('Resources', 'budget_data.csv')

#   open cvs file and read data

with open(py_bank_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Create list
    month_count = []
    profit_loss = []  
    change = []
    
    # Create  variables to hold data on first occurance
    previous = 0
    # Read each row of data after the header and store month and Profit lost data
    counter = 1 
    for row in csvreader: 
       
        month_count.append(row[0])
    
        profit_loss.append(float((row[1])))
             
        current =  (float((row[1])))
        if (int(counter) == 1):
            change_value = 0
            change.append(float(change_value)) 
        else:
            change_value = current - previous
            change.append(float(change_value)) 
        previous = (float((row[1])))
        counter = counter + 1 

# Collect variable for output         
change_avg = round(np.mean(change),3)
greatest_inc = np.max(change) 
greatest_dec = np.min(change)

# Zip list to extract month is the value is equal to max/min.
ziplist = (list(zip(range(86),month_count, profit_loss, change)))

# Collect output if the results match
for item in ziplist:

    Output_1 = (float((item[3]))) 
    if (int(greatest_inc) == Output_1):
        Result_1 = (f"Greatest Increase in Profits: {item[1]} (${item[3]})")
        print (Result_1)
    
    if (int(greatest_dec) == Output_1):
        Result_2 = (f"Greatest Decrease in Profits: {item[1]} (${item[3]})")
        print (Result_2)   

# Test print variables

net = sum(profit_loss)                  
print (row[0])
print (len(month_count))
print ('{:,}'.format(net))
print (change)      
print (change_avg)

# Print resuts to console
print ("Financial Analysis",
    "-------------------------",
    f"Total Month: {net}",
    f"Average Change $: {change_avg}",
    Result_1,
    Result_2, sep="\n")

# Create text file and output result 

output_file = os.path.join("Financial_Analysis.txt") 


with open(output_file , 'w') as f:
  sys.stdout = f
  
  print ("Financial Analysis",
    "-------------------------",
    f"Total Month: {net}",
    f"Average Change $: {change_avg}",
    Result_1,
    Result_2, sep="\n")






        
     
