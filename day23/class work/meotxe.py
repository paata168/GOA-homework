
last_name = input("Please enter your last name: ")


change_type = input("How would you like to change the case of your last name? (upper/lower/capitalize): ")


if change_type == "upper":
    print(last_name.upper())
elif change_type == "lower":
    print(last_name.lower())
elif change_type == "capitalize":
    print(last_name.capitalize())
else:
    print("Invalid option")
