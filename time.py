#!/usr/bin/env python
import time

#Tue Mar 10 00:41:49 2020
localtime = time.localtime()
#print(str(localtime.tm_year) + "" + str(localtime.tm_mon) + str(localtime.tm_mday))

localtime = time.strptime('%p')
print(localtime)