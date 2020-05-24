#Import Modules/ Path
import csv
import os
os.chdir("C:/Users/rsdut/Documents/GitHub/Python_project/PyPoll")
csvpath = os.path.join ("Homework03_Python_PyPoll.csv")

#Set variable initial value and Create variable lists
total_votes = 0
candidates_list =[]
unique_candidate =[]
vote_count =[]
vote_percent =[]

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #Start the loop to adress the questions
    for row in csvreader:
        total_votes +=1
        candidates_list.append(str(row[2]))


    for i in set(candidates_list):
        unique_candidate.append(i)
        cand_vote = candidates_list.count(i)
        vote_count.append(cand_vote)
        cand_vote_p = (cand_vote/total_votes)*100
        vote_percent.append(cand_vote_p)

#Find the winner of the election - using max number of votes
ind_max = vote_count.index(max(vote_count))
winner = unique_candidate[ind_max]


#Print outputs

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str('{:.3f}'.format(vote_percent[i])) + "% (" + str(vote_count[i]) + ")")          
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#Create a txt file to send the output prints
er = open("election_results.txt","w")

er.write("Election Results \n")
er.write("----------------------------------------------------------\n")
er.write("Total Votes :" + str(total_votes) + "\n")
er.write("----------------------------------------------------------\n")
for i in range(len(unique_candidate)):
    er.write(str(unique_candidate[i] + ": " + str('{:.3f}'.format(vote_percent[i])) + "% (" + str(vote_count[i]) +")" + "\n"))
er.write("----------------------------------------------------------\n")
er.write("The winner is: " + winner + "\n")
er.close()
