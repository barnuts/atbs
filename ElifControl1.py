#Vampire Hunter

print("Hello Master")
print("Can you please identify that this is your device?")
myName = str(input())

if myName == "Austin":
    print("Good, now just a few more questions, if you don't mind.")
    print("What is your age?")
    myAge = int(input())
    if myAge == 20:
        print("This does not prove just yet your identity.")
        print("What is your password?")
        myPw = input()
        if myPw == "3@Lr0G420":
            print("It is you master! *knotches silver-tipped crossbow bolt*")
        else:
            print("Your lucky day, but begone, this is serious business.")
    elif myAge <= 19:
        print("Get out of here kiddo, I don't want you getting hurt.")
    elif myAge >= 60:
        print("You are not the master of this device, Grandmama.")
else:
    print("Be gone, wretch.")
    
    
