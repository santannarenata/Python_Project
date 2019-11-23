#Import modules
import csv
import os

os.chdir("C:/Users/rsdut/Documents/GitHub/Python_challenge/PyBank")
csvpath = os.path.join("homework03_Python.csv")

#Create lists
profits =[]
date_p = []
monthly_changes = []

#set initial values for variables
l_count = 0

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #Start the loop to adress the questions
    for row in csvreader:
        l_count += 1
        profits.append(float(row[1]))
        date_p.append(str(row[0]))

for i in range(1,l_count):
    monthly_changes.append(profits[i] - profits[i-1])

#find index of maximum
ind_max = monthly_changes.index(max(monthly_changes)) + 1
ind_min = monthly_changes.index(min(monthly_changes)) + 1

print("Financial Analysis")
print("--------------------------------------------------------------------------------------------------------")
print("Total number of months included in the dataset is", l_count)
print("The net total amount of 'Profit/Losses' over the entire period is", sum(profits))
print("The average of the changes in 'Profit/Losses' over the entire period is", sum(monthly_changes)/(l_count-1))
print("Greatest increase is on", date_p[ind_max], "of value", max(monthly_changes))
print("Greatest decrease is on", date_p[ind_min], "of value", min(monthly_changes))


#creating a txt file to send the prints

fa = open("financial_analysis.txt","w")

fa.write("----------------------------------------------------------\n")
fa.write("Financial Analysis \n")
fa.write("----------------------------------------------------------\n")
fa.write("Total number of months included in the dataset is " + str(l_count) + "\n")
fa.write("The net total amount of 'Profit/Losses' over the entire period is " + str(sum(profits)) + "\n")
fa.write("The average of the changes in 'Profit/Losses' over the entire period is " + str(sum(monthly_changes)/(l_count-1)) + "\n")
fa.write("Greatest increase is on " + date_p[ind_max] + " of value " + str(max(monthly_changes))+ "\n")
fa.write("Greatest decrease is on " + date_p[ind_min] + " of value " + str(min(monthly_changes))+ "\n")
fa.write("----------------------------------------------------------\n")
fa.close()