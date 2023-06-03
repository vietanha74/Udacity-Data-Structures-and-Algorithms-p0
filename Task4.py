"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoingcalls = set()
incomingcalls = set()
outgoingtexts = set()
incomingtexts = set()
marketerphone = set()

for call in calls:
    outgoingcalls.add(call[0])
    incomingcalls.add(call[1])
for text in texts:
    outgoingtexts.add(text[0])
    incomingtexts.add(text[1])

for phone in outgoingcalls:
    if phone not in incomingcalls:
        if phone not in outgoingtexts and phone not in incomingtexts:
            marketerphone.add(phone)

print('These numbers could be telemarketers:')
for marketerphone in sorted(marketerphone):
    print(marketerphone)