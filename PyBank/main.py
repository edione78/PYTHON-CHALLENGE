#Importing the necessary modules/libraries
import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("../PyBank/Resources/budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row 
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl += int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    
paragraph = (
         f"Financial Analysis\n"
         f"---------------------\n"
         f"Total Months: {str(total_months)} \n"
         f"Total: ${str(total_pl)} \n"
         f"Average Change: ${str(round(avg_change,2))} \n"
         f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)}) \n"
         f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)}) \n"

)
#Displaying information
print(paragraph)
#Exporing to .txt file
output = open("output.txt", "w")


output.write(paragraph)