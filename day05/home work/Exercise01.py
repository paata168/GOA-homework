#1)მომხმარებელს შემოატანინეთ float სახის რიცხვი და შემდეგ ეგ რიცხვი გაყავით floor division-ის დახმარებით რომ იყოს integer და არა float

float_number = float(input("შეიყვანეთ რიცხვი წილადის სახით: "))

result = int(float_number)

print("თქვენი რიცხვი მთელი რიცხვის სახით არის: "+str(result))
