

# 재귀 연습 1

# def fib(num): 
#         if num <= 2:
#             return 1
#         else:
#             return fib(num-1) + fib(num-2)
    
# print(fib(10))



# 재귀 연습 2

# def facto(num):
#     if num <= 1:
#         return 1
#     else:
#         return num * facto(num-1)

# print(facto(8))


# # 클래스 정의
# class Person:
#     # 속성(변수)             - 클래스 변수
#     blood_color = 'red'

#     # 메서드

#     # 생성자 메서드,직접 호출 x
#     def __init__(self, name):
#         self.name = name         # - 인스턴스 변수
        
#     def singing(self):
#         return f'{self.name}가 노래합니다.'
    

# # 인스턴트 생성
# singer1 = Person('iu')
# singer2 = Person('BTS')



# #메서드 호출
# print(singer1.singing())
# print(singer2.singing())



# 인스턴스 메서드 구조

# # 인스턴스.메서드()
# 'hello'.upper()

# # 클래스.메서드(인스턴스 자기자신)

# str.upper('hello')



# 클래스 메서드 구조

# class MyClass:

#     @classmethod
#     def class_method(cls, arg1, ...):
#         pass



# 별 찍기 -10

# x = int(input())  # 3 9 27 81....

# def line(x):
#     for i in range(x):
#         print('*')


# def star(x):
#     if x <= 3:
#         pass
#     elif x > 3:
#         line(x)
        
# print(star(x))





# lee = ('***\n* *\n***')

# print(lee)



# N과 M - 1

# # num1 num2 는 str
# num1 , num2 = input().split()

# # 5, num2
# list_box = []
# for k in range(int(num1)):
#     list_box.append(k+1) 

# # num2개 짜리 중복제외를 만드는 코드 

# def wj(num2):
#     if num2 == 1:
#         for i in range(len(list_box)):
#             print (i)
    
#     else:
#         for j in wj(num2-1)





