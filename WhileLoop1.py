#Breaking out of a while loop

while True:
    print("Who are you?")
    name = str(input())
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (A hint: a fish for sport)")
    password = input()
    if password == "swordfish":
          break
print("Access Granted, Joe.")
    
