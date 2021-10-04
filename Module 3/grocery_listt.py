#create list
groceryList = ["Milk", "Bread", "Eggs", "Peanut Butter", "Jelly"]
print(groceryList)

#Change “peanut butter” in the list to “almond butter” using [] + indexing
groceryList[3] = "Almond butter"
print(groceryList)

#remove jelly using .remove()
groceryList.remove("Jelly")
print(groceryList)

#remove item using .pop() + indexing
groceryList.pop(1)
print(groceryList)

#add coffee to the list using .append()
groceryList.append("Coffee")
print(groceryList)