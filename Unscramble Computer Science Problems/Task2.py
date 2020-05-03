"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
all_numbers = []
outgoing = [calls[i][0] for i in range(len(calls))]
all_numbers.extend(outgoing)
incoming = [calls[i][1] for i in range(len(calls))]
all_numbers.extend(incoming)
all_numbers = set(all_numbers)
duration = [calls[i][3] for i in range(len(calls))]
zeros = [0]*len(calls)

duration_dic = dict(zip(all_numbers,zeros))
for i in range(len(calls)):
	for j in range(1):
		if calls[i][j] in all_numbers:
			duration_dic[calls[i][j]] += int(duration[i])

keymax = max(duration_dic, key=duration_dic.get)

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(keymax,duration_dic[keymax]) )
