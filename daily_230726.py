

# 1459. hw_7_2

# class StringRepeater:

#     def repeat_string(self, num, my_str):
#         for i in range(num):
#             print (my_str)
    
# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")



# 1460. hw_7_4

# class Person:
#     number_of_people = 0
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#         Person.number_of_people += 1

#     def introduce(self):
#         print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')
    
# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)



# 1454. ws_7_1

# class Shape:
   
#    def __init__(self,num1, num2):
#         self.width = num1
#         self.height = num2

# shape1 = Shape(5, 3)
# print(shape1.width, shape1.height)



# 1455. ws_7_2

# class Shape:
   
#     def __init__(self,num1,num2):
#         self.width = num1
#         self.height = num2

#     def calculate_area(self):
#         return self.width * self.height

# shape1 = Shape(5, 3)
# area1 = shape1.calculate_area()
# print(area1)



# 1456. ws_7_3

# class Shape:
   
#     def __init__(self,num1,num2):
#         self.width = num1
#         self.height = num2

#     def calculate_perimeter(self):
#         return (self.width + self.height) * 2

# shape1 = Shape(5, 3)
# perimeter1 = shape1.calculate_perimeter()
# print(perimeter1)



# 1457. ws_7_4

# class Shape:
   
#     def __init__(self,num1,num2):
#         self.width = num1
#         self.height = num2
#         self.area = num1 * num2
#         self.perimeter = (num1 + num2) * 2

#     def print_info(self):
#         print('Width:', self.width)
#         print('Height:', self.height)
#         print('Area:', self.area)
#         print('Perimeter:', self.perimeter)

# shape1 = Shape(5, 3)
# shape1.print_info()



# 1458. ws_7_5

# class Shape:
   
#     def __init__(self,num1, num2):
#         self.width = num1
#         self.height = num2

#     def __str__(self):
#         return f'Shape: width={self.width}, height={self.height}'

# shape1 = Shape(5, 3)
# print(shape1)
