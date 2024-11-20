#1)მომხმარებელს შემოატანინეთ float სახის რიცხვი და შემდეგ ეგ რიცხვი გაყავით floor division-ის დახმარებით რომ იყოს integer და არა float
# მომხმარებლისგან float რიცხვის მოთხოვნა
float_number = float(input("შეიყვანეთ რიცხვი (float ფორმატში): "))

# floor division-ის გამოყენება, რომ რიცხვი მთლიანად (integer) გამოვიდეს
result = float_number // 1

# შედეგის დაბეჭდვა
print(f"თქვენი რიცხვი მთლიანად (integer) არის: {result}")
