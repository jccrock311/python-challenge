# allows to create paths across operating systems
import os

# allows us to import our .csv file
import csv

# setting the paths for both the .csv and the output .txt files
pybank_dir = os.path.dirname(__file__)
csvpath = os.path.join(pybank_dir, "resources/budget_data.csv")
csvoutput = os.path.join(pybank_dir, "analysis/budget_output.txt")

# defining the initial variables being utilized
total_months = 0
total_money = 0
average_change = []
profit_loss = []
month = []

# opening the .csv and how to read it 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)    

    # for every row in the file...
    for row in csvreader:
        
        # iterate through these steps

        # obtains the total money starting at row 1
        total_money += int(row[1])

        # appends 'month' column to a new list
        month.append(row[0])

        # appends 'profits' to a new list
        profit_loss.append(int(row[1])) 

        # appends 'average change' and calculates the profits/losses differences
        average_change.append(profit_loss[total_months] - profit_loss[total_months - 1])

        # adds total amount of month in list
        total_months += 1

# calculates the 'average change' and rounds the decimal place to 2
total_change = sum(average_change)
change = round(total_change / (len(average_change) - 1), 2)

# gets the 'greatest increase in profits' and 'greatest decrease in profits'
great_increase = max(average_change)
great_decrease = min(average_change)

# gets the months associated with the 'greatest' values
increase_month = average_change.index(great_increase)
decrease_month = average_change.index(great_decrease)

# printing results to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_money)}")
print(f"Average Change: ${str(change)}")
print(f"Greatest Increase in Profits: {str(month[increase_month])}, ${str(great_increase)}")
print(f"Greatest Decrease in Profits: {str(month[decrease_month])}, ${str(great_decrease)}")

# creating the output .txt file and setting it up accordingly with '.write'
output = open(csvoutput, "w")

line1 = "Financial Analysis"
line2 = "----------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_money)}")
line5 = str(f"Average Change: ${str(change)}")
line6 = str(f"Greatest Increase in Profits: {str(month[increase_month])}, ${str(great_increase)}")
line7 = str(f"Greatest Decrease in Profits: {str(month[decrease_month])}, ${str(great_decrease)}")

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(line1, line2, line3, line4, line5, line6, line7))
