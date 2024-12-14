#1)შექმენით ფუნქცია რომელსაც გადაეცემა სია,გამოითვალეთ რიცხვების ჯამი for ციკლის საშუალებითაც და sum() ფუნქციის გამოყენებითაც აუცილებლად დააბრუნეთ შედეგი return ის გამოყენებით.

def calculate_sum(numbers):
    total_for =0
    for number in numbers:
        total_for+=number
        total_sum=sum(numbers)


        return total_for,total_sum
    
    numbers =[1,43,56,78]
    result_for,ressult_sum= calculate_sum(numbers)
    print("ჯამი for ციკლით", result_for)
    print("ჯამი sum()ფუნქციით",ressult_sum)