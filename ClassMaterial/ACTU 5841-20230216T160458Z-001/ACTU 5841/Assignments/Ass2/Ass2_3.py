# Reading the data from the CSV file

import csv

file = open('Lottery_NY_Lotto_Winning_Numbers.csv')

csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

file.close()

draws = []

row_num = range(len(rows))

# Populate 'draws' with winning numbers
# Split the winning number entries by empty space
# Append the bonus number to 'draws'
# Insert row number for each entries on the first column of 'draws'

for i in range(len(rows)):
    draws.append(rows[i][1])
    draws[i] = draws[i].split()
    draws[i].append(rows[i][2])
    draws[i].insert(0, row_num[i])

a = ['2', '02']

# Append the value of 'False' to all entries in 'draws'
# Update it to 'True' if the number 2 exists in that row
for i in range(len(draws)):
    draws[i].append(False)
    for j in range(1, 8):
        if draws[i][j] in a:
            draws[i][8] = True

index = []

# Identify the row numbers of entries that had '2' in the winning numbers or bonus #
for i in range(len(draws)):
    if draws[i][8] == True:
        index.append(draws[i][0])

gap = []

# Starting from the second index, calculate the gap by finding the difference in the indices
for i in range(1, len(index)):
    gap.append(index[i] - index[i - 1] - 1)
gap.sort()

import collections

# summarize the frequency of occurrence for each gap
frequency = collections.Counter(gap)

gap = list(frequency.keys())
count = list(frequency.values())

total = sum(count)
percent = list(map(lambda x: x / total, count))

header = ["GAP", "COUNT", "PERCENT"]
final = []

count_sum = 0
percent_sum = 0

# aggregating the occurrences and percentages with gaps greater than or equal to 10
for i in range(10, len(gap)):
    count_sum = count_sum + count[i]
    percent_sum = percent_sum + percent[i]

# formulating a summarized table with gaps 1 ~ 9 and >= 10
for i in range(11):
    final.append([gap[i], count[i], percent[i]])

gap[10] = chr(0x2265) + "10"
count[10] = count_sum
percent[10] = percent_sum

# Formating the final summary of results
print('number = 2')
print('%-5s%-6s%-8s' % (header[0], header[1], header[2]))
for i in range(0, len(final)):
    print('%-5s%-6i%-8f' % (gap[i], count[i], percent[i]))



