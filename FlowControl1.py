#This is your first flow control program

print("Hello World")
print("What is your name?")
myName = input()


if myName == str(myName):
    print("Hello " + myName + "," + " it is nice to meet you.")
    print("What would you like to set your password to?")
    myPw = input()
    if myPw == str(myPw):
        print("Your password has been set, would you like me to repeat it for you? Yes or no.")
        userInput = input()
        
        if userInput == "yes":
            print(myPw)
        elif userInput == "yesno":
            print("Haha, too funny. Your password has been sent to the nearest hacker.")
        else:
            print("I hope you wrote that down, " + myName + ".")
          
          
