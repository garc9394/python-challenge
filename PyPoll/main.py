import os
import csv
import pandas as pd

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
    total_votes = sum(1 for row in csvreader)

df = pd.read_csv(csvpath)
candidate_df = df.groupby('Candidate')['Voter ID'].count()

print()
print("Election Results")
print()
print("--------------------------")
print()
print("Total Votes: " + str(total_votes))
print()
print("--------------------------")
print()
for row in candidate_df:
    print(candidate_df[0])
    print()

file = open("report.txt", "w")
file.write("Election Results\n")
file.write("\n")
file.write("--------------------------\n")
file.write("\n")
file.write("Total Votes: " + str(total_votes) + "\n")
file.write("\n")
file.write("--------------------------\n")
file.write("\n")
file.close()