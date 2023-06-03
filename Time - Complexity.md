Task0:
This task take constant time -> O(1) 

Task1:
This task take linear time -> O(n) the access time for items in a list will take a linear time.
There are two loop iterator, each round for loop take O(n) so 2 loop iterator take O(n) + O(n) = O(2n)
-> Round off O(2n) into O(n)

Task2:
This task take linear time -> O(n) the access time for items in a list will take a linear time.
There are a loop iterator so it take O(n)

Task3:
Part A :
1. The first part of the code iterates through the "calls" list, which contains "n" elements. => O(n)
2. Sorting the "codes" set has a time complexity of O(m log m), where "m" is the number of unique codes.
3. Printing the codes has a time complexity of O(m), where "m" is the number of unique codes.
=> O(n + m + mlog m)
Part B: 
The iterates through the "calls" list, which contains "n" elements. => O(n)

Task4:
1. The first two for loops iterate through the "calls" and "texts" lists. Assume number of elements in the "calls" list is "n" and the number of elements in the "texts" list is "m"
=> O(m) + O(n) = O(m + n).
2. The third for loop iterate"outgoingcalls" set, which contains "k" elements (unique phone numbers). => O(k)
 -  Checking if a phone number  in a set => O(1)
 -  Adding elements to the "marketerphone" => O(1)
 => O(k)
3. Sorting the "marketerphone" set has a time complexity of O(j log j), where "j" is the number of elements in the set.

1 + 2 + 3 => O(n + m + k + j log j)
