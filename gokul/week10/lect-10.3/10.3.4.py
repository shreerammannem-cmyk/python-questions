# predict the output


class Student:
    def __init__(self,name,roll=None):
        self.name=name
        self.roll=roll


    def display(self):
        print(self.roll,self.name)

obj1=Student(1,"Gokul")
obj1.display() #gokul 1

obj2=Student(name="aswin")
obj2.display() #none aswin

obj3=Student("Gokul")
obj3.display() #none gokul

obj4=Student(roll=13)
obj4.display() #error