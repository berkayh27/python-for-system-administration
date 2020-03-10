#!/usr/bin/env python
import time

def gather_info():
    height = float(input("Please enter your height: "))
    weight = float(input("Please enter your weight: "))
    total = weight / height
    print(total) 

gather_info()

