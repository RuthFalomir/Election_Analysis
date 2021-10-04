x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7
while count <1:
    print("Hello World")

x = 1
y = 10
#checks if one value is equal to another
if x == 1:
    print("x is equal to 1")
    print("inside  the IF")

#checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")

if x >= 1:
    print("x is greater than or equal to 1")

if x==1 and y == 10:
    print("Both values returned true")

if x< 45 or y < 5:
    print("One or more were true")


####LOOPS


#loop thru a range of numbers (in this case 0 to 4)
for x in range(5):
    print(x)


#loop thru a range of numbers
for x in range (2,7):
    print(x)

#iterate thru letters in a string
word = "Peace"
for letters in word:
    print(letters) 

#loop while a condition is being met
run = "y"

while run == "y":
    print("Hi")
    run = input("To run again. Enter 'y'")