import csv
import os

# Set up variables to store results
total_months = 0
net_profit = 0
previous_profit = None
profit_changes = []
max_increase = {"date": "", "amount": 0}
max_decrease = {"date": "", "amount": 0}

# Open CSV file and read contents
budget_data_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip header row
    next(csv_reader)
    for row in csv_reader:
        # Update total number of months
        total_months += 1
        # Add profit/loss to net total
        net_profit += int(row[1])
        # Calculate change in profit from previous month (if applicable)
        if previous_profit is not None:
            change = int(row[1]) - previous_profit
            profit_changes.append(change)
            # Update max increase and decrease if necessary
            if change > max_increase["amount"]:
                max_increase["date"] = row[0]
                max_increase["amount"] = change
            elif change < max_decrease["amount"]:
                max_decrease["date"] = row[0]
                max_decrease["amount"] = change
        previous_profit = int(row[1])

# Calculate average change in profit/loss
average_change = sum(profit_changes) / len(profit_changes)

# Print results to terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase['date']} (${max_increase['amount']})")
print(f"Greatest Decrease in Profits: {max_decrease['date']} (${max_decrease['amount']})")

# Export results to text file
with open("financial_analysis.txt", "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_profit}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {max_increase['date']} (${max_increase['amount']})\n")
    txt_file.write(f"Greatest Decrease in Profits: {max_decrease['date']} (${max_decrease['amount']})\n")

print("Results exported to financial_analysis.txt")
