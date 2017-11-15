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
    total_votes = sum(1 for row in csvreader)

candidates = []
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)    # skip header row
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])

# votes_for_candidate = {'Candidate': [], 'Votes': []}
votes_for_candidate = {}
for x in candidates:
    vote_count = 0
    with open(csvpath, newline = "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        next(csvreader)    # skip header row
        for row in csvreader:
            if row[2] == x:
                vote_count = vote_count + 1
        # votes_for_candidate['Candidate'].append(x)
        # votes_for_candidate['Votes'].append(vote_count)
        votes_for_candidate[x] = vote_count
# print(votes_for_candidate)
# for Candidate, Votes in votes_for_candidate.items():
#     print(Candidate, Votes)



print()
print("Election Results")
print()
print("--------------------------")
print()
print("Total Votes: " + str(total_votes))
print()
print("--------------------------")
print()
# for l in range(0, len(votes_for_candidate['Candidate'])):
winner_vote_count = 0
for x in candidates:
    vote_count = 0
    with open(csvpath, newline = "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        next(csvreader)    # skip header row
        for row in csvreader:
            if row[2] == x:
                vote_count = vote_count + 1
        if vote_count > winner_vote_count:
            winner = x
            winner_vote_count = vote_count
        elif vote_count == winner_vote_count:
            winner = winner + " & " + x
        print(x + ": " + str(round(vote_count / total_votes * 100, 1)) + "% (" + str(vote_count) + ")")
        print()
print("--------------------------")
print()
print("Winner: " + winner)
print()
print("--------------------------")

file = open("report.txt", "w")
file.write("\n")
file.write("Election Results\n")
file.write("\n")
file.write("--------------------------\n")
file.write("\n")
file.write("Total Votes: " + str(total_votes) + "\n")
file.write("\n")
file.write("--------------------------\n")
file.write("\n")
winner_vote_count = 0
for x in candidates:
    vote_count = 0
    with open(csvpath, newline = "") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")
        next(csvreader)    # skip header row
        for row in csvreader:
            if row[2] == x:
                vote_count = vote_count + 1
        if vote_count > winner_vote_count:
            winner = x
            winner_vote_count = vote_count
        elif vote_count == winner_vote_count:
            winner = winner + " & " + x
        file.write(x + ": " + str(round(vote_count / total_votes * 100, 1)) + "% (" + str(vote_count) + ")\n")
        file.write("\n")
file.write("--------------------------\n")
file.write("\n")
file.write("Winner: " + winner + "\n")
file.write("\n")
file.write("--------------------------\n")
file.close()