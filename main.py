import random
from bloodyterminal import btext
import random_name

class Rectangle: #define the rectangle class
    def __init__(self, name, length, width):  #initiate the constructor and attributes
        self.name = name
        self.length = length
        self.width = width
    
    def area(self):  #method to calculate the area of a rectangle
        area = self.length * self.width
        return area
       
    def is_square(self):  #method that returns true if rectangle is also a square / else - false
        if self.length == self.width:
            return True
        else:
            return False
        
#test cases
a1 = random.randrange(1, 100)
a2 = random.randrange(1, 100)
rect = Rectangle(random_name.generate_name(), a1, a2)
rectArea=str(rect.area())
btext.success("The area of {0} is: {1}".format(random_name.generate_name(), rectArea))
input("Press enter to continue")