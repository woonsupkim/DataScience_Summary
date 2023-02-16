import csv

file = open('Lottery_NY_Lotto_Winning_Numbers.csv')

csvreader = csv.reader(file)
header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

file.close()


