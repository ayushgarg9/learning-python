class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def welcome(self):
        print("welcome", self.name)
    def get_marks(self):
        print(self.marks)

s1 = Student("ayush",97)
print(s1.name)
print(s1.marks)
s1.welcome()
s1.get_marks()

#to enter user name and details
class student:
    def __init__(self,name,m1,m2,m3,city,degree):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.city = city
        self.degree = degree
    
    def welcome(self):
        print("welcome", self.name)
        average = (self.m1+self.m2+self.m3)/3
        print("your average: ",average)
        print("wow", self.city)
        print("its ok to do", self.degree)

s1 = student("ayush",23,24,35,"patiala","engineering") #any random name given to start (it was thought by me not given anywhere)
s1.name = input("enter name: ")
s1.m1 = int(input("enter marks1: "))
s1.m2 = int(input("enter marks2: "))
s1.m3 = int(input("enter marks3: "))
s1.city = input("enter your city: ")
s1.degree = input("enter your degree: ")
s1.welcome()