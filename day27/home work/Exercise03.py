#3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი.

def number(num):
    if num<= 0:
        return("your number is negative")
    else:
        return("your number is positive") 
print(number(int(input("enter number: "))))        
       