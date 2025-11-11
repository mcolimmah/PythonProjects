## A Program that ask for your name and Password# Write your code here :-)

while True:
    print("Who are You? ")
    name = input(">")
    if name != "Joe":
        continue
    print("Hello, Joe. What is the Password? (It is a fish.)")
    password = input("......")
    if password == "swordfish":
          break

print("Access Granted.")
