#######################################################
# Example 1 for Object Oriented Programming - Classes #
#######################################################

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self, other): # sample class method
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5 

    def __str__(self): # when class is references through print fxn, return string version of class data
        return "<"+str(self.x)+","+str(self.y)+">"

c = Coordinate(3,4)
origin = Coordinate(0,0)

print("x-coord of c: ", c.x)
print("x-coord of origin: ",origin.x)

print("With Coordinate: ", Coordinate.distance(c,origin))
print("Without self: ", c.distance(origin)) # conventional

print(c)

print("use of insInstance: ", isinstance(c,Coordinate))

#######################################################
# Example 2 for Object Oriented Programming - Classes #
#######################################################

class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
    
    def __str__(self):
        return str(self.num)+"/"+str(self.denom)
    
    def __add__(self,other):
        # Returns the sum of 2 fraction
        top = self.num*other.denom + self.denom*other.num
        bot = self.denom*other.denom
        return Fraction(top,bot)

    def __sub__(self,other):
        # Returns the difference of 2 fraction
        top = self.num*other.denom - self.denom*other.num
        bot = self.denom*other.denom
        return Fraction(top,bot)

    def __float__(self):
        # Returns the float value of a fraction
        return self.num/self.denom
    
    def inverse(self):
        # Returns the inverse of a fraction
        return Fraction(self.denom,self.num)

frac1 = Fraction(2,5)
frac2 = Fraction(1,3)

print(frac1)
print(frac2)

frac3 = frac1+frac2 

print(frac3)
print(float(frac3))
print(Fraction.__float__(frac3))
print(frac2.inverse())
print(float(frac2.inverse()))

# Assignment # 1


    # ASEAN Country              Code
    # Federation of Malaysia      60
    # Republic of Indonesia       62
    # Republic of the Philippines 63
    # Republic of Singapore       65
    # Kingdom of Thailand         66

    # Main Menu 

    # f the user selects an invalid option, the menu should keep on showing.

    # [1] Store to ASEAN phonebook
    # [2] Edit entry in ASEAN phonebook
    # [3] Search ASEAN phonebook by country 
    # [4] Exit

    # [1] Store to ASEAN phonebook

    # Enter student number: 2004-56
    # Enter surname: Lee
    # Enter first name: Sukarno
    # Enter occupation: Doctor
    # Enter gender (M for male, F for female): M Enter country code: 63
    # Enter area code: 2
    # Enter number: 4567890
    # Do you want to enter another entry [Y/N]? N

    # After entering all information, ask the user whether he wants to add another entry, 
    # in which case a new set of prompting should happen. Otherwise, go back to the main menu.

    # [2] Edit entry in ASEAN phonebook

    # Ask the user first for the student number. 
    # If it does not exist, alert an error. Otherwise, editing should proceed, as displayed below (the “edit menu”):

    # Enter student number: 2004-56
    # Here is the existing information about 2004-56:
    # Sukarno Lee is a Doctor. His number is 63-2-4567890
    # Which of the following information do you wish to change?

    # [1] Student number [4] Occupation   [7] Phone Number   
    # [2] Surname        [5] Country code [8] None - Back to Main Menu 
    # [3] Gender         [6] Area Code
    # Enter choice: 1
    # Enter new student number: 2005-67

    # After the new information has been entered, the “edit menu” should again show, 
    # now displaying the modified information. The said menu should keep on showing until the user selects 8.

    # [3] Search ASEAN phonebook by country

    # The user can also view students only from specified countries. He can select single or multiple countries. 
    # Once the countries are chosen, print all the students (with their corresponding information) from those countries. 
    # Printed student-entries should be alphabetically arranged according to surname. 
    # Furthermore, if [6] ALL is selected, all students from all countries should be shown. 
    # If zero [0]  is entered, that means, no more countries are to be included in the search. 
    # After printing, go back to main menu. Follow this:

    # From which country:
    # [1] Philippines [2] Thailand [3] Singapore [4] Indonesia [5] Malaysia [6] ALL [0] No More
    # Enter choice 1: 1
    # Enter choice 2: 2
    # Enter choice 3: 0 
    # Here are the students from Philippines and Thailand:
    # Saint, John, with student number 2000-123, is a doctor. His phone number is 63-2- 9998765
    # Krap, Sawadi, with student number 1999-890, is a sorcerer. His phone number is 66-8-1234567
    # Dela Cruz, Juliana, with student number 1991-000, is a princess. Her phone number is 63-6-678123890

    # objects: Country, Person, Main Menu, Store Menu, Edit Menu, Search Menu
    # Country : country_name, country_code,
    #           getCountryName(), getCountryCode()

    
class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0 for i in range(num_sides)]
    
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.num_sides)]

    def showSides(self):
        for i in range(self.num_sides):
            print("Side: "+(i+1)+" is ",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)    
    
    def findArea(self):
        a,b,c = self.sides

        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5

        print("The area of the triangle is %0.2f" %area)

class Fan(object):
    def __init__(self,is_used,brand):
        self.is_used = is_used
        self.brand = brand
    
    def use_the_fan(self,is_used):
        self.is_used = True

my_bool = False
fan_ko = Fan(my_bool,"Nike")

fan_ko.use_the_fan(my_bool)
print(fan_ko.is_used)

print(fan_ko.brand)