###################################
# INTERPOL, which stands for Integer Program Oriented Language, is a language specifically designed for IS 214 students. 
# Compared to its IS 214 predecessors, INTERPOL is the simplest of them all. 
# What makes it “integer oriented” is that the PL primarily deals with integers and consequently, 
# no floating-point values are allowed. 
# This implies that the results of arithmetic operations are automatically converted to integers. 
# Strings are also allowed for printing purposes.
# The goal of this programming assignment is to implement an INTERPOL interpreter using Python, 
# which you have learned at the beginning of the semester. You may accomplish the assignment individually or by pair. 
# Your interpreter should be able to perform the following:
#   Accept expressions from the user.
#   Parse the code entered by the user and check for lexical and syntax errors.
#   Properly execute INTERPOL expressions by the user.
#   Spaces are used to demarcate tokens in the language.
#   Multiple spaces and tabs are treated as single spaces and are otherwise considered irrelevant.
#   Indentation is also irrelevant.
#   INTERPOL is case sensitive.

#INTERPOL only has one section. 
# The section begins with the CREATE keyword and ends with the RUPTURE keyword. 
# All coding - variable declarations and actual instructions - are to be placed between these keywords.

# CREATE	
# DSTR stringmo WITH [I have a pen]
# GIVEYOU!! stringmo
# DINT x WITH PLUS 1 MINUS 9 9	
# DINT y	
# STORE 100 IN y	
# GIVEYOU!! x	
# GIVEYOU! y	
# RUPTURE

# Output:
# I have a pen
# 1
# 100

DINT,DST,STORE = "DINT","DSTR","STORE"
PLUS,MINUS,MULT,DIV,MODU = "PLUS","MINUS","MULT","DIV","MODU"

class Token(object):
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type},{value})'.format(type = self.type, value = repr(self.value))

    def __repr__(self):
        return self.__str__()

# There are only 2 main data types: integer and string.
# The interpreter shall follow the principles of strong typing. 
# Therefore, intermixing of integers and strings in arithmetic operations is not allowed.
# All variables are declared and are global in scope.
# Any attempts to use floating-point values should result to an error.
# A string is enclosed by square brackets.

# Declaring an integer variable without an initial value: DINT <variable_name>
# Declaring an integer variable with an initial value: DINT <variable_name> WITH <expression>
# Declaring a string variable without an initial value: DSTR <variable_name>
# Declaring a string variable with an initial value: DSTR <variable_name> WITH <expression>

# Assignment: STORE <expression> IN <variable>

# An expression can be a literal/value, a variable, or it can be composed of several adjacent operators. 
# Hence, nested expressions should be successfully implemented as well in your interpreter.


# InterpolBody is for the processing of the entire code block
class InterpolBody(object):

    def __init__(self,code_block):
        self = self
        self.code_block = code_block
    
    def processBlock(self):

        # process code block
        # segregate code blocks
        # create tokens
        
        temp_tokens = []

        for i in range(len(self.code_block)):
            
            temp_tokens = self.code_block[i].replace('\t','').split(' ')
            
            if self.checkGrammar(temp_tokens) == True:
                print("correct grammar")
            
            else:
                print("Syntax Error! Invalid syntax")

            print(temp_tokens)
            
            i+=1

        return self
    
    def checkGrammar(self,block_line):

        symbol_table = []
        lexemes = []
        tokens = []

        isDeclaration = False
        isAssignment = False

        startToken = 0
        token_type = ""

        for i in range(len(block_line)):
            # check if declaration
            # check type of declaration
            if (block_line[i] == DINT or block_line[i] == DST) and i==0:
                
                isDeclaration = True
                startToken = 1
                token_type = "Identifier"

            if block_line[i] == STORE and i==0:
                
                isAssignment = True
                startToken = 1
                token_type = "Identifier"  
                
            elif isinstance(block_line[i],int):
                token_type = "Integer"
            
            elif block_line[i] == "WITH" or block_line[i] == "IN":
                token_type = "Identifier"
            
            elif block_line[i] == PLUS or block_line[i] == MINUS or block_line[i] == DIV or block_line[i] == MULT or block_line[i] == DIV or block_line[i] == MODU:
                token_type = "Expression"

            symbol_table.append(Token(token_type,block_line[i]))
            i+=1
        
        print(symbol_table)
                 
        # check if assignment
        # check if expression
        return True

    def checkContext(self):
        return self
    
    def getResult(self):
        return self.code_block


class InputOutput(object):
    def __init__(self):
        self = self

    def inputFromUser(self):
        # Asking input from the user:  GIVEME? <variable_name>
        return input("GIVEME? ")    

    def printOutput(self,tag,output_block):
        if tag == 1:
            # Printing values, variables, and expressions: GIVEYOU! <expression>
            return print("GIVEYOU!",output_block)
        elif tag == 2:
            # Printing values, variables, and expressions with a new line affixed at the end: GIVEYOU!! <expression>
            return print("GIVEYOU!",output_block,"\n")


class ArithmeticOperations(object):
    import math

    def __init__(self,arith_values):
        self = self
        self.arith_values = arith_values
    
    def add(self,val1,val2):
        # Addition: PLUS <expression1> <expression2>
        return val1+val2
    
    def sub(self,val1,val2):
        # Subtraction: MINUS <expression1> <expression2>
        return val1-val2
    
    def mul(self,val1,val2):
        # Multiplication: TIMES <expression1> <expression2>
        return val1*val2
    
    def div(self,val1,val2):
        # Division: DIVBY <expression1> <expression2>
        return val1/val2
    
    def mod(self,val1,val2):
        # Modulo: MODU <expression1> <expression2>
        return val1%val2

class AdvancedArithmetic(ArithmeticOperations):
    def __init__(self):
        self = self
    
    def exp(self,expr,expo):
        # Exponentiation: RAISE <expression> <exponent>
        return expr**expo

    def nthRoot(self,N,expr):
        # Nth Root of a No. : ROOT <N> <expression>
        return expr

    def avg(self,values):
        # Average: MEAN <expr1> <expr2> <expr3> … <exprn>
        #  This is the only operation that accepts an unlimited number of parameters.
        return values

    def distance(self,pt1,pt2):
        # Distance between two points: DIST <expr1> <expr2> AND <expr3> <expr4>
        # #  The 2 points are separated by ‘AND’
        # #  The coordinates of the first point are <expression1> and <expression2> 
        # #  The coordinates of the second point are <expression3> and <expression4>
        return (pt2[1]-pt1[1])+(pt2[0]-pt1[0])

def readIpolFile():
    # read indicated .ipol file

    return True

def checkIpolFile():
    # verifies if .ipol file is valid
     return True

def main():
    # TEST FOR INTERPRETER. NOT ACTUAL INPUT METHOD
    block_end = False
    block_start = False
    code_block = []

    while block_end == False:
        text_input = input('interpol>')
        if text_input == "CREATE":
            # start reading in cobe block
            block_start = True

        elif text_input == "RUPTURE":
            block_end = True
            break
        
        elif block_start == True:
            code_block.append(text_input)

    # process code block
    code_block = InterpolBody(code_block)
    code_block.processBlock()
    print(code_block.getResult())

main()
# Do not use graphical user interface, databases (eg. MySQL), and other unnecessary libraries in Python. 
# Focus on what’s core in this assignment – the interpreter itself.
# Your interface should be command line.
# Implement your interpreter with the following use case in mind:
#   a)	The user writes his INTERPOL source code using any text editor. Take note that the source code has “.ipol” extension.
#   b)	From the command prompt, the user runs your interpreter. Your interpreter then asks for the file name of the .ipol code to be executed.
#   c)	Still in the command prompt, the following outputs are displayed to the user:
#           Actual output of the source code
#  If there’s an error, the user should be informed of the error and possibly, the source of the error.
#           Symbol table
#           Lexemes and tokens table

# Submission
# Submit your programming assignment on or before Monday, 25 November 2017 at 11:59:59 pm (GMT+8).
# Your assignment should be in a single Python source code that contains your implementation of the INTERPOL interpreter.
# Filename:  (all lowercase letters please) surname.py (if solo) or surname1_surname2.py (if by pair).
# This is the file that I will immediately compile and run to test out your interpreter.
# Please don’t forget to document your code properly by using comments. 
