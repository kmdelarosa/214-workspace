print("Hello World!")

###############################
#    Write Data in Python     #
###############################
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # two stars are used for exponentiation (2 to the power of 16)
print(37 / 3)  # single forward slash is a division
print(37 // 3)  # double forward slash is an integer division
        # it returns only the quotient of the division (i.e. no remainder)
print(37 % 3)  # percent sign is a modulus operator
        # it gives the remainder of the left value divided by the right value

###############################
#    Read Data in Python      #
###############################
print('What is your name?')
name = input()  # read a single line and store it in the variable "name"
print('Hi ' + name + '!')

###############################
#    Operators in Python      #
###############################

## Addition
a = input()
b = input()
s = a + b
print(s)

################################
# Integer Arithmetic in Python #
################################

import math # for modules used for float calculations
from math import ceil

x = math.ceil(4.2) # return the ceiling value (the smallest integer not let that 4.2)

x = 7 / 2
y = ceil(x)
print(y)

print(abs(-6))
print(abs(3.81))
print(abs(0))

# Rounding values
math.floor(x) # floor value (largest integer less than or equal to x)
math.ceil(x) # return the ceiling value (the smallest integer not less that x)

# Roots and logarithms
math.sqrt(x) # square root of x
math.log(x)  # With one argument, return the natural logarithm of x (to base e). 
             # With two arguments, return the logarithm of x to the given base
math.e       # mathematical constant e

# Trigonometry
math.sin(x)  # sin value of x radians
math.asin(x) # arcsin of x radians
math.pi      # mathematica constant pi = 3.1415... 

#######################
# Recursion and Loops #
#######################

for i in range(5, 8):
    print(i, i ** 2)
print('end of loop')
# 5 25
# 6 36
# 7 49
# end of loop

for i in range(3): # min_value = 0      
    print(i)
# 0
# 1
# 2

for i in range(2 ** 2):
    print('Hello, world!')

for i in range(-5): # won't execure for block, considered empty range
    print('Hello, world!')

for i in range(7,3): # won't execure for block, considered empty range
    print('Hello, world!')

# sum of integers from 1 to n, inclusively
result = 0
n = 5
for i in range(1, n + 1):
    result += i
    # this ^^ is the shorthand for
    # result = result + i
print(result)

# iterate over a decreasing sequence, we can use an extended form of range() with three arguments - 
# range(start_value, end_value, step)

for i in range(10, 0, -2):
    print(i)
# 10
# 8
# 6
# 4
# 2

# sep and end in print()
print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep=', ', end='. ')
print(4, 5, 6, sep=', ', end='. ')
print()
print(1, 2, 3, sep='', end=' -- ')
print(4, 5, 6, sep=' * ', end='.')

# sample use of +=, -=, *=, and /=
result = 0
debt = 1000
prod = 1
divine = 100
n = 5
for i in range(1, n + 1):
    result += i   # the same as result = result + i
    debt -= i     # the same as debt = debt - i
    prod *= i     # the same as prod = prod * i
    divine /= i     # the same as divine = divine / i
print(result)
print(debt)
print(prod)
print(divine)

# decreasing iteration
for i in range(10, 0, -2):
    print(i)
# 10
# 8
# 6
# 4
# 2

###########
# Strings #
###########

print('>_< ' * 5)  # >_< >_< >_< >_< >_<

len() # return num of characters in a string
print(len('abcdefghijklmnopqrstuvwxyz'))  # 26

str() # converts any object in python to string

s = str(2 ** 100)
print(s)  # 1267650600228229401496703205376
print(len(s))  # 31

S = 'Hello' 

S[0] == 'H', S[1] == 'e', S[2] == 'l', S[3] == 'l', S[4] == 'o'
S[-1] == 'o', S[-2] == 'l', S[-3] == 'l', S[-4] == 'e', S[-5] == 'H'

S[a:b] # returns the substring of length b - a, starting with the character at index a and lasting until the character at index b, 
       # not including the last one

S[1:4] == 'ell'
S[-4:-1]

S[1:-1] # substring without the first and the last character of the string

S[1:] # to remove the first character at index 0
S[:-1] # removes the last character of the string
S[:] # return the string itself

# immutability of strings
s = 'Hello'
t = s  # s and t point to the same string
t = s[2:4]  # now t points to the new string 'll'
print(s)  # prints 'Hello' as s is not changed
print(t)  # prints 'll'

d=1

S[a:b:d] # third parameter specifies the step
a, a + d, a + 2 * d # not including the character with index b
d = -1 # characters go in reverse order
S[::-1] # reverse a string

s = 'abcdefg'
print(s[1])
print(s[-1])
print(s[1:3])
print(s[1:-1])
print(s[:3])
print(s[2:])
print(s[:-1])
print(s[::2])
print(s[1::2])
print(s[::-1])

s = 'abcdefghijklm'
print(s[0:10:2])
for i in range(0, 10, 2):
    print(i, s[i])

s.find("e") # searches a substring, passed as an argument, inside the string on which it's called
            # returns the index of the first occurrence of the substring. 
            # If the substring is not found, the method returns -1

s = 'Hello'
print(s.find('e'))
# 1
print(s.find('ll'))
# 2
print(s.find('L'))
# -1

s.rfind('a') # returns the index of the last occurrence of the substring

s = 'abracadabra'
print(s.find('b'))
# 1
print(s.rfind('b'))
# 8

# s.find(substring, left, right) # search is performed inside the slice s[left:right]
#s.find(substring, left) # search is performed in the slice s[left:], that is, 
                        # starting with the character at index left to the end of the string
#s.find(substring, left, right) # returns the absolute index, relatively to the whole string s, and not to the slice

s = 'my name is bond, james bond, okay?'
print(s.find('bond'))
# 11
print(s.find('bond', 12))
# 23

# replace() # replaces all occurrences of a given substring with another one.
old, new,count,substring = 0,0,0," "
s.replace(old, new) # takes the string S and replaces all occurrences of substring old with the substring new

print('a bar is a bar, essentially'.replace('bar', 'pub'))
# 'a pub is a pub, essentially'

s.replace(old, new, count) #  replace only first count occurrences and then stop
print('a bar is a bar, essentially'.replace('bar', 'pub', 1))
# 'a pub is a bar, essentially'

s.count(substring) # counts the number of occurrences of one string within another string
                   # Only non-overlapping occurrences are taken into account

print('Abracadabra'.count('a'))
# 4
print(('aaaaaaaaaa').count('aa'))
# 5

left, right = 1, 1

s.count(substring, left, right) # count is performed within the slice s[left:right]

##############
# While Loop #
##############


# while some condition:
 #   a block of statements

# fragment prints the squares of all integers from 1 to 10
while i <= 10:
    print(i ** 2)
    i += 1

# determine the number of digits of an integer n
n = int(input())
length = 0
while n > 0:
    n //= 10  # this is equivalent to n = n // 10
    length += 1
print(length)  # 4

# while with an else statement
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print('Loop ended, i =', i)

# Black Jack-like example: a program that reads numbers and sums it until the total gets greater or equal to 21. 
# The input sequence ends with 0 for the program to be able to stop even if the total sum of all numbers is less than 21.

total_sum = 0
a = int(input())
while a != 0:
    total_sum += a
    if total_sum >= 21:
        print('Total sum is', total_sum)
        break
    a = int(input())
else:
    print('Total sum is less than 21 and is equal to', total_sum, '.')

# for loop with else
# a program reads 5 integers but stops right when the first negative integer is met.

for i in range(5):
    a = int(input())
    if a < 0:
        print('Met a negative number', a)
        break
else:
    print('No negative numbers met')

# continue
# If Python interpreter meets continue somewhere in the middle of the loop iteration, 
# it skips all the remaining instructions and proceeds to the next iteration.

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# Multiple Assignment

a, b = 0, 1

a = 1
b = 2
a, b = b, a
print(a, b)
# 2 1

#########
# Lists #
#########

# Like the characters in the string, the list elements can also have negative index, 
# for example, Primes[-1] == 13, Primes[-6] == 2. The negative index means we start at the last element and go left when reading a list.

Rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(Rainbow[0])
Rainbow[0] = 'red'
print('Print the rainbow')
for i in range(len(Rainbow)):
    print(Rainbow[i])

# First of all, you can create an empty list (the list with no items, its length is 0), 
# and you can add items to the end of your list using append.

a = [] # start an empty list
n = int(input()) # read number of element in the list
for i in range(n): 
    new_element = int(input()) # read next element
    a.append(new_element) # add it to the list
    # the last two lines could be replaced by one:
    # a.append(int(input()))
print(a)

a = []
for i in range(int(input())):
    a.append(int(input()))
print(a)

# There are several operations defined for lists: list concatenation (addition of lists, i.e. "gluing" one list to another) 
# and repetition (multiplying a list by a number).

a = [1, 2, 3]
b = [4, 5]
c = a + b
d = b * 3
print([7, 8] + [9])
print([0, 1] * 3)

a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    print(a[i])

a = [1, 2, 3, 4, 5]
for elem in a:
    print(elem, end=' ')

# Sequences in Python are strings, lists, values of the function range() (these are not lists), and some other objects.
# use of the for loop when you are needed to extract all the digits from a string and to make numeric list of them.

# given: s = 'ab12c59p7dq'
# you need to extract digits from the list s
# to make it so:
# digits == [1, 2, 5, 9, 7]
s = 'ab12c59p7dq'
digits = []
for symbol in s:
    if '1234567890'.find(symbol) != -1:
        digits.append(int(symbol))
print(digits)

# List items can be given in one line separated by a character; in this case, the entire list can be read using input(). 
# You can then use a string method split(), which returns a list of strings resulting after cutting the initial string by spaces. Example:

# the input is a string
# 1 2 3
s = input() # s == '1 2 3'
a = s.split() # a == ['1', '2', '3']
print(a)

a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

# Using the special magic of Python — generators — the same can be done in one line:

a = [int(s) for s in input().split()]
print(a)

# the method split() has an optional parameter that determines which string will be used as the separator between list items. 
# For example, calling the method split('.') returns the list obtained by splitting the initial string where the character '.' 
# is encountered:

a = '192.168.0.1'.split('.')
print(a)

# In Python, you can display a list of strings using one-line commands. 

a = ['red', 'green', 'blue']
print(' '.join(a))
# return red green blue
print(''.join(a))
# return redgreenblue
print('***'.join(a))
# returns red***green***blue

# If a list consists of numbers, you have to use the dark magic of generators.
# Here's how you can print out the elements of a list, separated by spaces:

a = [1, 2, 3]
print(' '.join([str(i) for i in a]))
# the next line causes a type error,
# as join() can only concatenate strs
# print(' '.join(a))

# To create a list filled with identical items, you can use the repetition of list, for example:

n = 5
a = [0] * n
print(a)

# To create more complicated lists you can use generators: the expressions allowing to fill a list according to a formula. 
# The general form of a generator is as follows:

# [expression for variable in sequence]

# variable is the ID of some variable, 
# sequence is a sequence of values, which takes the variable (this can be a list, a string, or an object obtained using the function range), 
# expression — some expression, usually depending on the variable used in the generator. 
# The list elements will be filled according to this expression.

a = [0 for i in range(5)]
print(a)

n = 5
a = [i ** 2 for i in range(n)]
print(a)

# If you need to fill out a list of squares of numbers from 1 to n, you can change the settings of range to range(1, n + 1)

n = 5
a = [i ** 2 for i in range(1, n + 1)]
print(a)

# Here's how you can get a list filled with random numbers from 1 to 9 (using randrange from the module random):

from random import randrange
n = 10
a = [randrange(1, 10) for i in range(n)]
print(a)

# the list will consist of lines read from standard input: first, you need to enter the number of elements of the list 
# (this value will be used as an argument of the function range), second — that number of strings:

a = [input() for i in range(int(input()))]
print(a)

# With lists and strings, you can do slices. Namely:

A = []

j,k = 0,0

A[i:j]  # slice j-i elements A[i], A[i+1], ..., A[j-1].

A[i:j:-1]  # slice i-j elements A[i], A[i-1], ..., A[j+1] (that is, changing the order of the elements).

A[i:j:k]  # cut with the step k: A[i], A[i+k], A[i+2*k],... . If the value of k<0, the elements come in the opposite order.

A = [1, 2, 3, 4, 5]
A[2:4] = [7, 8, 9]
print(A) # [1, 2, 7, 8, 9, 5]

A = [1, 2, 3, 4, 5, 6, 7]
A[::-2] = [10, 20, 30, 40]
print(A) # [40, 2, 30, 4, 20, 6, 10]

# operations on lists

x in A # Check whether an item in the list. Returns True or False
x not in A # The same as not(x in A)
min(A) # The smallest element of list
max(A) # The largest element in the list
A.index(x) # The index of the first occurrence of element x in the list; in its absence generates an exception ValueError
A.count(x) # The number of occurrences of element x in the list

 


