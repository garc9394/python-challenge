import os
import csv

file_list = []
x = 0

for file in os.listdir("raw_data"):
    if file.endswith(".csv"):
        file_list.insert(x, os.path.join(file))
        x += x

file_list.sort()

for file_name in file_list:
    print("[" + str(file_list.index(file_name)) + "] " + file_name)

# ask user as to which of the two files to open for analysis

selection = int(input("Which file do you want to open? "))
csvpath = ('raw_data/' + file_list[selection])

# for verifications
# with open(csvpath, newline = "") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter = ",")
#     for row in csvreader:
#         print(row)

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)    # skip header row
    total_month = sum(1 for row in csvreader)

total_revenue = 0
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        total_revenue = row[1]
        try:
            total_revenue = int(total_revenue)
        except ValueError:
            total_revenue = 0
        total_revenue += total_revenue

average_revenue_change = total_revenue / total_month

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)    # skip header row
    max_increase = max(int(column[1].replace(',', '')) for column in csvreader)

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for index, row in enumerate(csvreader):
        if row[1] == str(max_increase):
            max_increase_month = row[0]

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)    # skip header row
    max_decrease = min(int(column[1].replace(',', '')) for column in csvreader)

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for index, row in enumerate(csvreader):
        if row[1] == str(max_decrease):
            max_decrease_month = row[0]


print()
print("Financial Analysis")
print()
print("--------------------------")
print()
print("Total Months: " + str(total_month))
print()
print("Total Revenue: $" + str(total_revenue))
print()
print("Average Revenue Change: $" + str(int(average_revenue_change)))
print()
print("Greatest Increase in Revenue: " + max_increase_month + " ($" + str(max_increase) + ")")
print()
print("Greatest Decrease in Revenue: " + max_decrease_month + " ($" + str(max_decrease) + ")")
print()

# export to text file

file = open("report.txt", "w")
file.write("Financial Analysis\n")
file.write("\n")
file.write("--------------------------\n")
file.write("\n")
file.write("Total Months: " + str(total_month) + "\n")
file.write("\n")
file.write("Total Revenue: $" + str(total_revenue) + "\n")
file.write("\n")
file.write("Average Revenue Change: $" + str(int(average_revenue_change)) + "\n")
file.write("\n")
file.write("Greatest Increase in Revenue: " + max_increase_month + " ($" + str(max_increase) + ")\n")
file.write("\n")
file.write("Greatest Decrease in Revenue: " + max_decrease_month + " ($" + str(max_decrease) + ")\n")
file.close()