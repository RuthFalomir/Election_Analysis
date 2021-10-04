#Pseudocode
##the data we need to retreive
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
import os

import csv

   
#  NOT WORKING
#assign a variable for the file to load and the path
#file_to_load = 'Resources\election_results.csv'

#open the election results and read the file
#election_data = open(file_to_load,'r')
#election_data.close()



file_to_load = os.path.join('Resources','election_results.csv')

file_to_save = os.path.join("analysis","election_analysis,txt")

#create variable to hold rows aka ACCUMULATOR
total_votes = 0

#create a new list to add candidate names
candidate_options = []

#create empty dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    #to do: read and analyze data here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #lines = file_handler.read()
    #print(election_data)

    #for row in file_reader:
        #print(row)

    #read the header row
    headers = next(file_reader)

    # print each row in the csv file
    for row in file_reader:
        total_votes += 1
        
        #print the candidate name from each row
        candidate_name = row[2]
        
        #if the candidate_name doesn't match any existing candidate
        if candidate_name not in candidate_options:
        
        #add it to the list of candidates
            candidate_options.append(candidate_name)

        #begin tracking that candidates vote count  
            candidate_votes[candidate_name] = 0

    #add a vote to that candidates count
        candidate_votes[candidate_name] += 1

    #determine the percentage of votes for each candidate by looping thru the count
    #1. iterate thru the candidate list:
    for candidate_name in candidate_votes:
        #2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #3. calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #4. Print the candidate name & percentage votes
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #determine the winning vote count and candidate
        #1. determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. if true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3. Set the winning_candidate = candidate_name
            winning_candidate = candidate_name
        

    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)

print(total_votes)
print(candidate_options)
print(candidate_votes)
#### Writing on file with open() & close() functions from os
##create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis","election_analysis,txt")
##using the open() function with the "w" mode we will write data to the file
#outfile = open(file_to_save,"w")
#outfile.write("Hello World")
#outfile.close()

#### Writing on file using with statement

#with open(file_to_save,"w") as txt_file:
    #Write data to the file
    #txt_file.write("Hello World")
    ##first method, addding one by one
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    #txt_file.close()
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    #txt_file.write("Arapahoe\nDenver\nJefferson")