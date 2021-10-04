counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties")

if 'Arapahoe' in counties and 'El Paso' in counties:
    print('Arapahoe and El Paso are in the list of counties.')
else:
    print('Arapahoe or El Paso is not in the list of counties.')


if 'Arapahoe' in counties or 'El Paso' in counties:
    print('Arapahoe or El Paso is in the list of counties.')
else:
    print('Arapahoe and El Paso are not in the list of counties.')

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[1])

for i in range(len(counties)):
    print(counties[i])

counties_tuples = ("Arapahoe","Denver","Jefferson")

for i in range(len(counties_tuples)):
    print(counties_tuples[i])


counties_dict = {"Arapahoe": 422829,"Denver": 463353,"Jefferson": 432438}
print(counties_dict)

for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)


for  voters in counties_dict.values():
    print(voters)

print(counties_dict["Denver"])

#modify the for loop and use the key, county to reference the value.
for county in counties_dict:
    print(counties_dict[county])

#if we want to print the key-value pair of the dictionary, we use the items() method in the for loop
for key, value in counties_dict.items():
    print(key,value)
for county, voters in counties_dict.items():
    print(county,voters)
    
for county, voters in counties_dict.items():
    print(str(county) + " county has", str(voters) + " registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])
    
#print the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])

#f strings
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#f strings with dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}"
    f"You received {candidate_votes/total_votes*100}% of the total votes."
    )
print(message_to_candidate)

candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,"
    f"You received {candidate_votes/total_votes*100:.2f}% of the total votes."
    )
print(message_to_candidate)

#pwd - print working directory
#cd - change directory
#cd.. - move up one directory
#mkdir - creates new folder
#explorer .- open the current directory
#code . - opens VScode
#touch<file_name - creates a file
#ls - shows folder contents