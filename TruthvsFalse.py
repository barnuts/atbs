#Truthey and Falsey Values

name = " "
while not name:
    print("Enter your name: ")
    name = str(input())
print("How many guests will you be caring for tonight?")
numOfGuests = int(input())
if numOfGuests:
    print("Be sure to have enough room for all of your guests.")
print("Done")
