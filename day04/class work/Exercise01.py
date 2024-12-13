first_name = input("შეიყვანეთ თქვენი სახელი: ")
last_name = input("შეიყვანეთ თქვენი გვარი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

print(f"{first_name} {last_name} არის {age} წლის.")

age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age % 2 == 0:
    print("თქვენი ასაკი არის ლუწი.")
else:
    print("თქვენი ასაკი არის კენტი.")
