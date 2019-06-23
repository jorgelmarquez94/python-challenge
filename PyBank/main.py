# Import dependencies
import os
import csv
import operator

# Declaration of variables
months = []
profit_losses = []
revenue_changes = []

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Function to get number of months
def number_of_months(months):
	return len(months)

# Function to get total profit/losses
def total_profit_losses(profit_losses):
    total = 0
    for ele in range(0, len(profit_losses)):
        total = total + int(profit_losses[ele])
    return total

# Function to get the average change of profit
def average_change(profit_losses):
    change_profit = 0

    for ele in range(len(profit_losses)-1):
        last_profit = int(profit_losses[ele])
        current_profit = int(profit_losses[ele+1])
        avg_current_profit = current_profit - last_profit
        change_profit += avg_current_profit
        revenue_changes.append(avg_current_profit)
    return round(change_profit / (len(profit_losses)-1),2)

# Function to get the index with the max change of profit
def greatest_increase(revenue_changes):
    index, max_value = max(enumerate(revenue_changes), key=operator.itemgetter(1))
    return index

# Function to get the index with the min change of profit
def greatest_decrease(revenue_changes):
    index, min_value = min(enumerate(revenue_changes), key=operator.itemgetter(1))
    return index

# Function to print the results
def print_results():
    print("Financial Analysis")
    print("----------------------------")
    print("Total months: " + str(number_of_months(months)))
    print("Total: $" + str(total_profit_losses(profit_losses)))
    print("Average change: $" + str(average_change(profit_losses)))
    print("Greatest Increase in Profits: " + str(months[greatest_increase(revenue_changes)+1]) + " ($" + str(revenue_changes[greatest_increase(revenue_changes)]) + ")")
    print("Greatest Decrease in Profits: " + str(months[greatest_decrease(revenue_changes)+1]) + " ($" + str(revenue_changes[greatest_decrease(revenue_changes)]) + ")")

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(row[1])

    print_results()


# Set variable for output file
output_file = os.path.join("financial_analysis.txt")

# Open the output file
with open(output_file,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write("Total months: " + str(number_of_months(months)) + "\n")
    text.write("Total: $" + str(total_profit_losses(profit_losses)) + "\n")
    text.write("Average change: $" + str(average_change(profit_losses)) + "\n")
    text.write("Greatest Increase in Profits: " + str(months[greatest_increase(revenue_changes)+1]) + " ($" + str(revenue_changes[greatest_increase(revenue_changes)]) + ")" + "\n")
    text.write("Greatest Decrease in Profits: " + str(months[greatest_decrease(revenue_changes)+1]) + " ($" + str(revenue_changes[greatest_decrease(revenue_changes)]) + ")" + "\n")