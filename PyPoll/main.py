import csv
import os
os.chdir("C:/Users/rsdut/Documents/GitHub/Python_challenge/PyPoll")
csvpath = os.path.join ("Homework03_Python_PyPoll.csv")

total_votes = 0
candidates_list =[]

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvfile:
        total_vote =+1
        candidates_list.append(str(row[2]))

