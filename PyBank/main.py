import os
import csv

# Full path to the CSV file
csv_path = os.path.join("PyBank", "Resources", "budget_data.csv.csv")

# Initialize variables
total_months = 0
net_total = 0
prev_profit = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        date = row[0]
        profit = int(row[1])

        # Calculate the total number of months
        total_months += 1

        # Calculate the net total amount
        net_total += profit

        # Calculate the change in profit
        if total_months > 1:
            change = profit - prev_profit
            profit_changes.append(change)

            # Identify the greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase[0] = date
                greatest_increase[1] = change

            # Identify the greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease[0] = date
                greatest_decrease[1] = change

        # Store the current profit for the next iteration
        prev_profit = profit

# Calculate the average change
average_change = sum(profit_changes) / (total_months - 1)

# Prepare the results
results = (
    "Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
output_file = os.path.join("PyBank", "Analysis", "analysis.txt")
with open(output_file, "w") as textfile:
    textfile.write(results)