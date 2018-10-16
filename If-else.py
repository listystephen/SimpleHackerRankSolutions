Problem
--------

Task 
Given an integer,n , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird



Soln
*****

#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())

if (N%2 != 0) or (N in range(6,22,2)):
    print"Weird"
else:
    if (N%2 == 0 and N > 20) or  (N in range(2,5,2)):
        print "Not Weird"