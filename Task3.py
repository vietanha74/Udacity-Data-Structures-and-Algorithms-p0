"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
telephone_numbers = set()
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
   
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Create a set to store the codes of the receiving numbers
codes = set()
for call in calls:
    if call[0].startswith('(080)'):
        receiving_number = call[1]
        if receiving_number.startswith('('):
            # Fixed line number
            code = receiving_number.split(')')[0] + ')'
        elif  receiving_number.startswith(('7','8','9')):
            code = receiving_number[:4]
        elif receiving_number.startswith('140'):
            # Telemarketer number
            code = '140'
        codes.add(code)
#=>O(1)
# Print the answer message
print("The numbers called by people in Bangalore have codes:")
for code in sorted(codes): #=>O(m log m), Sorting the "codes" set has a time complexity of O(m log m), where "m" is the number of unique codes.
    print(code) #=> O(m)

print("######################################################################")
#PART B
NumberRecvFrom080 = 0
Number080 = 0
for call in calls:
    if call[0].startswith('(080)'):
        receiving_number = call[1]
        Number080 += 1
        if receiving_number.startswith('('):
            # Fixed line number
            code = receiving_number.split(')')[0] + ')'
            if code == '(080)':
              NumberRecvFrom080 += 1

percent = (float(NumberRecvFrom080)/float(Number080))*100
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(round(percent, 2)))
