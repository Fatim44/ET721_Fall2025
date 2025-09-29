"""

Fatima Nadeem
Lab 7, accessing data in a file 
Sep 29, 2025
"""
from lab7_function import *

testing()
print("\n ---- example 1: reading file -----")
with open("phrases.txt",'r') as fileuser:
    eachline = fileuser.readlines()
# use a loop to go over each line in fileuser 
for each in fileuser:
    print(each)
read_data("phrases.txt")