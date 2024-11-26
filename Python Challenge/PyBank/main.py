# import csv file
import csv
import os

# source to read revenue data file
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Define variables 
total_months = 1
total_net = 0
average_change = []
months = []

# Open the csv and reading it 
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

     # Extract first row 
    FirstRow = next(reader)

    PreviousNet = float(FirstRow[1])

   # Process each row of data
    for row in reader:
   
   # Track the total 
        total_months += 1

        # calculate net change 
        total_net += float(row[1])
        net_change = float(row[1]) - PreviousNet 
        average_change.append(net_change)
        PreviousNet = float(row[1])

        # add the first month that changed 
        months.append(row[0]) 

       # calculate the average net change 
averageChangePerMonth = sum(average_change) / len(average_change)

GreatestIncrease = [months[0], average_change[0]]
GreatestDecrease = [months[0], average_change[0]]

# loop through the index of the greatest and the decrease monthly change
for m in range(len(average_change)):
    # calculate the greatest increase and decrease
    if(average_change[m] > GreatestIncrease[1]):
        GreatestIncrease[1] = average_change[m]
        GreatestIncrease[0] = months[m]

    if(average_change[m] < GreatestDecrease[1]):
        GreatestDecrease[1] = average_change[m]
        GreatestDecrease[0] = months[m]

# making the output 
output =f"""
Financial Analysis
----------------------------
Total Months = {total_months}
Total Net = ${total_net:,.2f}
Average Change Per Month = ${averageChangePerMonth:,.2f}
Greatest Increase in Profits = ${GreatestIncrease[0]} Amount ${GreatestIncrease[1]:,.2f}
Greatest Decrease in Profits = ${GreatestDecrease[0]} Amount ${GreatestDecrease[1]:,.2f}
"""
      
# Print the output
print(output)

# export the output to the output text file
with open(file_to_output, "w") as textfile:
    textfile.write(output)
    
       




