petDictionary = {
    "name":"Maggi",
    "age":14,
    "hobbies":("sleeping", "walking", "eating"),
    "wakeUpHours":{
        "monday":6,
        "tuesday":7,
        "friday":9
    }
}   
print(petDictionary)

#Print out Your pet's name and age.
print(f'{petDictionary["name"]} is {petDictionary["age"]} years old.')

#Print How many hobbies your pet has.
print(f'{petDictionary["name"]} has {len(petDictionary["hobbies"])} hobbies.')

#Print What your pet's favorite hobby is.
print(f'{petDictionary["name"]} loves to spend the afternoon {petDictionary["hobbies"][1]}.')

#Print What time your pet wakes on one of the days of the week.
print(f'{petDictionary["name"]} wakes up at {petDictionary["wakeUpHours"]["monday"]} AM.')