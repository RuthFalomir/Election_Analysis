#string variable
name = "Ruth Falomir"

#float variable
salary = 123.75

#integer variable
age = 20

#empty variable
message = ""

#boolean variable
isWeatherWarm = True

#print function + concatenation (adding more than one string together)
print("My name is " + name)

#str function (turns integers into strings)
print("My age is " + str(age))

name = "Ruth Falomir"
country = "Mexico"
age = 27
hourlyWage = 20
satisfied = True
dailyWage = hourlyWage * 8

print("My name is " + name)
print("My country is " + country)
print("My age is " + str(age))
print("I make " + str(hourlyWage) + " per hour.")
print("I make " + str(dailyWage) + " a day.")


#f string
print(f"My name is {name} and I am from {country}. I am {age} years old. I earn {hourlyWage} per hour and {dailyWage} a day.")


###LISTS 

#create a list
myList = ["Ruth", "Raquel", "Rebeca", "Esther"]
print(myList)

#create empty list
emptyList = []

#add elements to list
myList.append("Mama")
print(myList)

#return the index of the first object with a matching value
print(myList.index("Rebeca"))

#change a specified element within a list at a given index
myList[0] = "Roberta"
print(myList)

#return length of the list
print(len(myList))

#remove a specified objetc from a list
myList.remove("Roberta")
print(myList)

####TUPLES (immutable -cant be changed)

#create a tuple 
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)

#print specified items in a tuple using indexing
print(myTuple[0])

#print the length of a tuple using len() function
print(len(myTuple))


####DICTIONARIES

#create a dictionary (key, value)
pacman = {
    'isAlive': True,
    'points': 380,
    'lives': 7
}

#create a dictionary that includes a LIST as one of the variables
actor = {
    "name": "Ana",
    "Age": 20,
    "movies":[
        "Rocky",
        "Rocky 2",
        "Rocky 3"]}
print(f'{actor["name"]} was in {actor["movies"][0]}')

#create a dictionary that contains another DICTIONARY
film = {
    "title":"Interstellar",
    "revenues": {
        "United States":360,
        "China":250,
        "United Kingdom":73
    }
}
print(f'{film["title"]} made {film["revenues"]["United States"]}'" in the US.")

#create a dictionary including a TUPLE
myTuple2 = ("1",99,"Alarm","Dell","Oracle")

myDictionary = {
    "brand":"IBM",
    "listTuple":myTuple2
}

print(myDictionary)
