# class myClass():
#     def __init__(self, str):
#         self.str = str
    
#     def getString(self):
#         self.str = input()

#     def printString(self):
#         print(self.str.upper())
        
# a = myClass("hello")
# a.getString()
# a.printString()

#-----------------------------------
# class Shape():
#     def __init__(self, len):
#         self.len = len
#     def area(self):
#         return 0
         
# class Square(Shape):
#     def area(self):
#         return self.len*self.len

# shape = Shape(6)
# square = Square(8)  
# print(shape.area())  
# print(square.area())

#-------------------------------------
# class Shape():
#     def __init__(self, len):
#         self.len = len
#     def area(self):
#         return 0
         
# class Square(Shape):
#     def area(self): 
#         return self.len*self.len

# class Rectangle(Shape):
#     def __init__(self, len, width):
#         self.len = len
#         self.width = width
#     def area(self):
#         return self.len*self.width

# shape = Shape(6)
# square = Square(8)  
# rectangle = Rectangle(8, 4) 
# print(shape.area())  
# print(square.area())   
# print(rectangle.area())  
#---------------------------------

# import math

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print("(" + str(self.x) + ";" + str(self.y) + ")")
#     def move(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#         print("(" + str(self.x) + ";" + str(self.y) + ")")
#     def dist(self, x2, y2):
#         self.x2 = x2
#         self.y2 = y2
#         distance = math.sqrt((self.x-self.x2)**2 + (self.y-self.y2)**2)
#         print(distance)

# obj = Point(5, 2)
# obj.show()
# obj.move(6,3)
# obj.show()
# obj.dist(7,6)

#--------------------------------------
# class BankAcc():
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def withdraw(self):
#         self.balance 
