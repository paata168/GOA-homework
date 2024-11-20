#კომენტარებით ახსენით რას აკეთებს str(), int(), და float() ფუნქციები:


# str() - ფუნქცია გადაქცევს მონაცემს სტრინგის ტიპად
num = 123
num_str = str(num)  # აქ num-ს მთელი რიცხვი (int) გადავქცევით სტრინგად
print(type(num_str))  # <class 'str'>

# int() - ფუნქცია კონვერტირებას ახდენს სტრინგსა თუ სხვა ტიპის მონაცემს მთელ რიცხვად (integer)
str_num = "45"
num = int(str_num)  # აქ str_num-ს სტრინგიდან მთელ რიცხვად ვაქცევთ
print(type(num))  # <class 'int'>

# float() - ფუნქცია გადაქცევას ახდენს მონაცემს მრუდი რიცხვად (float)
num_str = "3.14"
num_float = float(num_str)  # აქ სტრინგი ვაქცევთ მრუდი რიცხვად
print(type(num_float))  # <class 'float'>
