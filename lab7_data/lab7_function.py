"""

Fatima Nadeem
Lab 7, accessing data in a file (functions)
Sep 29, 2025
"""
def testing():
    print("FATIMA NADEEM")

# EXAMPLE 1: read file
def read_data(filename):
    # pipe a text line in a file with a Phython code
    fileuser = open(filename, 'r')

    # use a loop to go over each line in filesuer
    for each in fileuser:
        print(each)