import os 
import sys 

# This is used to sum items in array

array1 = [1,2,3,4,5]

def arraySummer(ar):
    zeroo = 0
    for elements in ar:
        zeroo += elements
    return zeroo

output_for_me = arraySummer(array1)
print(output_for_me)