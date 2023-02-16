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

for i in range(len(rows)):
    draws.append(rows[i][1])
    draws[i] = draws[i].split()
    draws[i].append(rows[i][2])
    draws[i].insert(0,row_num[i])

a = ['2', '02']

for i in range(len(draws)):
    draws[i].append(False)
    for j in range(1,8):
        if draws[i][j] in a:
            draws[i][8] = True

index = []
index.append(0)
for i in range(len(draws)):
    if draws[i][8] == True:
        index.append(draws[i][0])

gap = []
for i in range(1, len(index)):
    gap.append(index[i] - index[i-1]-1)
gap.sort()


import collections
frequency = collections.Counter(gap)

gap = list(frequency.keys())
count = list(frequency.values())

total = sum(count)
percent = list(map(lambda x: x / total, count))

header = ["GAP", "COUNT", "PERCENT"]

count_sum = 0
percent_sum = 0

for i in range(10, len(gap)):
    count_sum = count_sum + count[i]
    percent_sum = percent_sum + percent[i]

with open('sanity_check.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', )
    writer.writerow(header)

    for i in range(10, len(gap)):
        count_sum = count_sum + count[i]
        percent_sum = percent_sum + percent[i]

    for i in range(10):
        writer.writerow([gap[i], count[i], percent[i]])

    gap[10] = ">=10"
    writer.writerow([gap[10], count_sum, percent_sum])
    file.close()

file = open('sanity_check.csv')

csvreader = csv.reader(file)

final = []
for row in csvreader:
    final.append(row)

file.close()

print('number = 2')
print(final)


with open('sanity_check.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)