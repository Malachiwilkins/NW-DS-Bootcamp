# Create files across operating systems
import os
# Read CSV file
import csv
csvpath = os.path.join("budget_data.csv")
# Open CSV File
with open(csvpath) as csvfile:
# CSV reader identifies the deliimiter and [1: ] skips header and goes till there isn't a number anymore
    reader = list(csv.reader(csvfile, delimiter=","))[1:]
# Set variables
    months = [row[0] for row in reader]
    amount = [int(row[1]) for row in reader]
    months_total = len(months)
totalmoney = sum(amount)
# Creates a function to find out the profit/loss difference between rows of profit loss numbers
differences = [amount[i+1]-amount[i] for i in range(len(amount)-1)]

# Find the average change of the differences from rows
averagediff=sum(differences)/months_total
# Getting the Greatest increase & Greatest decrease using the min and max functions
Greatest_Increase = max(differences)
Greatest_Decrease = min(differences)
# Accounting for the months with the GreatestInc and GreatestDec number
Greatestmonthindex = differences.index(Greatest_Decrease)
Greatestmonthincrease = months[Greatestmonthindex]

#Print title
print("Financial Analysis")
print("----------------------------------")

# Print statements
print("Total Months:", months_total)
print("Total: $", totalmoney)
print("Average: $", averagediff)
print("Greatest Increase in Profits:" , Greatestmonthincrease, Greatest_Increase)
print("Greatest Decrease in Profits:", Greatestmonthincrease, Greatest_Decrease)

    
    
    