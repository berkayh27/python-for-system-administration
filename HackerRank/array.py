import os 
import sys 

# This is used to sum items in array
# any array that is given will print out the to

array1 = [1,2,3,4,5]

def arraySummer(anything_that_user_gives):
    total_now = 0
    for elements in anything_that_user_gives:
        total_now += elements
    return total_now

output_for_me = arraySummer(array1)
print(output_for_me)