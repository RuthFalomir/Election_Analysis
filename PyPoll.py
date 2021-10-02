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

with open(file_to_load) as election_data:
    #to do: read and analyze data here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)
    #lines = file_handler.read()
    #print(election_data)
    #print each row in the csv file
    
    #for row in file_reader:
        #print(row)

    headers = next(file_reader)
    print(headers)
#### Writing on file with open() & close() functions from os
##create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join("analysis","election_analysis,txt")
##using the open() function with the "w" mode we will write data to the file
#outfile = open(file_to_save,"w")
#outfile.write("Hello World")
#outfile.close()

#### Writing on file using with statement

with open(file_to_save,"w") as txt_file:
    #Write data to the file
    #txt_file.write("Hello World")
    ##first method, addding one by one
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    #txt_file.close()
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    #txt_file.write("Arapahoe\nDenver\nJefferson")