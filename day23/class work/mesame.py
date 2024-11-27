
name = input("Please enter your name: ")


character = input("Please enter a character to search for: ")


index = name.find(character)

if index == -1:
    print("Can't find character")
else:
    print("Found it")
    print("The index of the character is:", index)
