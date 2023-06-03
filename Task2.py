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
"""
list_total_time = []
telephone_numbers = set()

for call in calls:
    telephone_numbers.add(call[0])
    telephone_numbers.add(call[1])

for telephone_number in telephone_numbers:
    total_time = 0
    for text in calls:
        if telephone_number == text[0] or telephone_number == text[1]:
            total_time += int(text[3])
    list_total_time.append((telephone_number,total_time))    

sorted_list = sorted(list_total_time, key=lambda total_time: total_time[1])
len = len(sorted_list)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(sorted_list[len-1][0], sorted_list[len-1][1]))
"""
# Dictionary to keep track of all calls
phonenumber = {}  # O(1)

for call in calls:  # O(n)
    if call[0] not in phonenumber:
        phonenumber[call[0]] = int(call[3])  #O(1)
    else :
        phonenumber[call[0]] += int(call[3]) #O(1)
    if call[1] not in phonenumber:
        phonenumber[call[1]] = int(call[3])  #O(1)
    else:
        phonenumber[call[1]] += int(call[3]) #O(1)

sorted_list = sorted(phonenumber.items(), key=lambda total_time: total_time[1])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(sorted_list[-1][0], sorted_list[-1][1]))