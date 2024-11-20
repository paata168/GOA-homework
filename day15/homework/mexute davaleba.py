original_password = "saidumlo1232"  
user_password = input("შეიყვანეთ თქვენი პაროლი: ")

while user_password != original_password:
    user_password = input("არასწორი პაროლი. სცადეთ კიდევ ერთხელ: ")

print("პაროლი სწორი არის!")
