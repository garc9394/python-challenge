import io
import csv


csvpath1 = ('raw_data/budget_data_1.csv')
csvpath2 = ('raw_data/budget_data_2.csv')

# for verifications
# with open(csvpath1, newline = "") as csvfile1:
#     csvreader1 = csv.reader(csvfile1, delimiter = ",")
#     for row in csvreader1:
#         print(row)

with open(csvpath1, newline = "") as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter = ",")