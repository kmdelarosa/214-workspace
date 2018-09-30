###########################
# 4. For loops with range #
###########################

# 1. Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

a = int(input())
b = int(input())

for i in range(a,b+1):
    print(i)

# 2. Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, 
# if A < B, or in descending order, if A ≥ B.

a = int(input())
b = int(input())

if(a<b):
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)

# 3. 10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.

sum = 0

for i in range(10):
    temp = int(input())
    sum += temp

print(sum)

# 4. N numbers are given in the input. Read them and print their sum. 
# The first line of input contains the integer N, which is the number of integers to follow. 
# Each of the next N lines contains one integer. Print the sum of these N integers.

N = int(input())

sum = 0

for i in range(N):
    temp = int(input())
    sum += temp

print(sum)

# 5. For the given integer N calculate the following sum: 1**3+2**3+…+N**3

N = int(input())

sum = 0

for i in range(1,N+1):
    sum += i**3

print(sum)

# 6. In mathematics, the factorial of an integer n, denoted by n! is the following product: n!=1×2×…×n

n = int(input())

f = 1

for i in range (1,n+1):
    f *= i

print(f)

# 7. Given N numbers: the first number in the input is N, after that N integers are given. 
# Count the number of zeros among the given integers and print it. 
# You need to count the number of numbers that are equal to zero, not the number of zero digits.

N = int(input())

count = 0
for i in range(N):
    temp = int(input())
    
    if(temp==0):
        count += 1

print(count)

# 8. Given an integer n, print the sum 1!+2!+3!+...+n!. 
# This problem has a solution with only one loop, so try to discover it. And don't use the math library :)

n = int(input())

sum = 0
f = 1

for i in range(1,n+1):
    f *= i
    sum += f
    
print(sum)

# 9. For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them. 
# To do that, you can use the sep and end arguments for the function print().

n = int(input())

if(n <= 9):
    for i in range(1,n+1):
        for a in range(1,i+1):
            print(a, end='')
        print()

# There was a set of cards with numbers from 1 to N. One of the card is now lost. 
# Determine the number on that lost card given the numbers for the remaining cards.
# Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards 
# (distinct integers in the range from 1 to N). Find and print the number on the lost card.

N = int(input())

sum = 0
sum_temp = 0
for i in range(1, N+1):
    sum += i

for a in range(1,N):
    temp = int(input())
    sum_temp += temp

print(sum - sum_temp)

#############
# 5. String #
#############

# 1. You are given a string.
# In the first line, print the third character of this string.
# In the second line, print the second to last character of this string.
# In the third line, print the first five characters of this string.
# In the fourth line, print all but the last two characters of this string.
# In the fifth line, print all the characters of this string with even indices 
# (remember indexing starts at 0, so the characters are displayed starting with the first).
# In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).
# In the seventh line, print all the characters of the string in reverse order.
# In the eighth line, print every second character of the string in reverse order, starting from the last one.
# In the ninth line, print the length of the given string.

s = input()

print(s[2])
print(s[-2])
print(s[0:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# 2. Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method count.

s = input()
print(s.count(' ')+1)

# 3. Given a string. Cut it into two "equal" parts (If the length of the string is odd, place the center character in the first string, 
# so that the first string contains one more characther than the second). Now print a new string on a single row with the first and 
# second halfs interchanged (second half first and the first half second)Don't use the statement if in this task.

s = input()

a = s[:int(len(s)/2)+(len(s)%2)]
b = s[int(len(s)/2)+(len(s)%2):]

print(b,a, sep = "")

# 4. Given a string consisting of exactly two words separated by a space. Print a new string with the first and second word positions 
# swapped (the second word is printed first).
# This task should not use loops and if.

s = input()
print(s[s.find(' ')+1:],s[:s.find(' ')])

# 5. Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f. 
# If the letter f occurs only once, then output its index. If the letter f does not occur, then do not print anything.
# Don't use loops in this task.

s = input()

f = s.find('f')
r = s.rfind('f')

if(f != r):
    print(f,r)
elif(f != -1):
    print(f)
else:
    print("")

# 6. Given a string that may or may not contain the letter of interest. Print the index location of the second occurrence of the letter f. 
# If the string contains the letter f only once, then print -1, and if the string does not contain the letter f, then print -2.

s = input()

if s.find('f') == -1:
    print(-2)
elif s.find('f') == s.rfind('f'):
    print(-1)
else:
    print(s.find('f',s.find('f')+1))

# 7. Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, 
# as well as all the characters between them.

s = input()
print(s[:s.find('h')],s[s.rfind('h')+1:],sep='')

# 8. Given a string in which the letter h occurs at least two times, 
# reverse the sequence of characters enclosed between the first and last appearances.

s = input()
m = s[s.find('h'):s.rfind('h')+1]
print(s[:s.find('h')],m[::-1],s[s.rfind('h')+1:],sep='')

# 9. Given a string. Replace in this string all the numbers 1 by the word one.

s = input()
print(s.replace('1','one'))

# 10. Given a string. Remove from this string all the characters @.

s = input()
print(s.replace('@',''))

# 11. Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.

s = input()
print(s[:s.find('h')+1],s[s.find('h')+1:s.rfind('h')].replace('h','H'),s[s.rfind('h'):],sep='')

# 12. Given a string. Delete from it all the characters whose indices are divisible by 3.

s = input()
m = ""
for i in range(len(s)):
    if i%3 != 0:
        m += s[i]
print(m)

##################
# 5. While Loops #
##################

# 1. For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order.

N = int(input())

i=1

while i**2 <= N:
    print(i**2)
    i += 1

# 2. Given an integer not less than 2. Print its smallest integer divisor greater than 1.

n = int(input())

i = 2

while n%i != 0:
    i += 1

print(i)

# 3. For a given integer N, find the greatest integer x where 2x is less than or equal to N. 
# Print the exponent value and the result of the expression 2x.
# Don't use the operation **.

N = int(input())

e, i = 2, 1

while e <= N:
    e *= 2
    i += 1

print(i-1,int(e/2),sep=' ')

# 4. As a future athlete you just started your practice for an upcoming event. 
# Given that on the first day you run x miles, and by the event you must be able to run y miles.
# Calculate the number of days required for you to finally reach the required distance for the event, 
# if you increases your distance each day by 10% from the previous day.
# 
# Print one integer representing the number of days to reach the required distance.

x = int(input())
y = int(input())

d = 1

while x < y:
    x += (x*.10)
    d += 1

print(d)

# 5. Given a sequence of non-negative integers, where each number is written in a separate line. 
# Determine the length of the sequence, where the sequence ends when the integer is equal to 0. 
# Print the length of the sequence (not counting the integer 0). The numbers following the number 0 should be omitted.

n = int(input())

i = 0
while n > 0:
    i+=1
    n = int(input())

print(i)

# 6. Determine the sum of all elements in the sequence, ending with the number 0.

sum = 0
n = int(input())

while n != 0:
    sum += n
    n = int(input())

print(sum)

# 7. Determine the average of all elements of the sequence ending with the number 0.

sum, count = 0, 0
n = int(input())

while n != 0:
    sum += n
    count += 1
    n = int(input())

print(sum/count)

# 8. A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence.

l = 0
n = int(input())

while n != 0:
    if l < n:
        l = n
    n = int(input())

print(l)

# 9. A sequence consists of integer numbers and ends with the number 0. 
# Determine the index of the largest element of the sequence. 
# If the highest element is not unique, print the index of the first of them.

l,i,c = 0,0,0
n = -1

while n != 0:
    n = int(input())
    i += 1
    
    if l < n:
        l = n
        c = i
   
print(c)

# 10. Determine the number of even elements in the sequence ending with the number 0.

n,count = -1,0

while n != 0:
    if n%2 == 0:
        count += 1
    n = int(input())

print(count)

# 11. A sequence consists of integer numbers and ends with the number 0. 
# Determine how many elements of this sequence are greater than their neighbours above.

t,n,count = -1,-1,0

while n != 0:
    n = int(input())
    if n > t:
        count += 1
    t = n
    
print(count-1)

# 12. The sequence consists of distinct positive integer numbers and ends with the number 0. 
# Determine the value of the second largest element in this sequence. It is guaranteed that the sequence has at least two elements.

l,s = 0,0

n = int(input())

while n!=0:
    if n >= l:
        s = l
        l = n
    elif s<= n <= l:
        s = n
    n = int(input())  

print(s)

# 13. A sequence consists of integer numbers and ends with the number 0. 
# Determine how many elements of this sequence are equal to its largest element.

l,c = 0,0
n = int(input())

while n != 0:
    if l < n:
        l,c = n,1
    elif n == l:
        c += 1
    n = int(input())

print(c)

# 14. The Fibonacci sequence is defined as follows: ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
# Given a non-negative integer n, print the nth Fibonacci number ϕn.
# This problem can also be solved with a for loop.

n = int(input())
t,f,i = 0,0,2

if n > 0:
    f = 1
    while i <= n:
     t,f = f,t+f
     i+=1
print(f) 

# 15. The Fibonacci sequence is defined as follows: ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2. 
# Given an integer a, determine its index among the Fibonacci numbers, that is, print the number n such that ϕn=a. 
# If a is not a Fibonacci number, print -1.

alpha = int(input())

f1,f2= 0,0

if alpha > 0:
    f2,i = 1,1
    
    while f2 <= alpha:
        if f2 == alpha:
            print(i)
            break
        f1,f2 = f2,f1+f2
        i+=1
    else:
        print(-1)

# 16. Given a sequence of integer numbers ending with the number 0. 
# Determine the length of the widest fragment where all the elements are equal to each other.

p,c = 0,1
n,l = -1,0

while n != 0:
    n = int(input())
    if p==n:
        c+=1
    else:
        if c > l:
            l = c
        c=1
    p = n
print(l)

#########
# Lists #
#########

# 1. Given a list of numbers, find and print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...).

a = input().split()

for i in range(len(a)):
    if i%2 == 0:
        print(a[i])

# 2. Given a list of numbers, find and print all elements that are an even number. 
# In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range()

a = input().split()
b = []
for i in a:
    if int(i)%2==0:
        b.append((i))
print(' '.join(b))

# 3. Given a list of numbers, find and print all the elements that are greater than the previous element.

n = [int(i) for i in input().split()]
p = n[0]

for i in n:
    if i > p:
        print(i)
    p=i

# 4. Given a list of numbers, find and print the first adjacent elements which have the same sign. 
# If there is no such pair, leave the output blank.

n = [int(i) for i in input().split()]
for i in range(1, len(n)):
    if n[i-1] > 0 < n[i] or n[i-1] < 0 > n[i]:
        print(n[i-1],n[i])
        break

# 5. Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors. 
# The first and the last items of the list shouldn't be considered because they don't have two neighbors.

n = [int(i) for i in input().split()]
c = 0
for i in range(2, len(n)):
    if n[i-2] < n[i-1] > n[i]:
        c+=1
print(c)

# 6. Given a list of numbers. Determine the element in the list with the largest value. 
# Print the value of the largest element and then the index number. 
# If the highest element is not unique, print the index of the first instance.

n = [int(i) for i in input().split()]
l,d = n[0],0

for i in range(1,len(n)):
    if n[i]>l and n[i] != l:
        l,d = n[i],i
print(l, d)

# 7. Given a list of numbers with all of its elements sorted in ascending order, 
# determine and print the quantity of distinct elements in it.

n = [int(i) for i in input().split()]
ctr = 1
for i in range(1,len(n)):
    if n[i] != n[i-1]:
        ctr+=1
print(ctr)

# 8. Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. 
# If a list has an odd number of elements, leave the last element in place.

n = [int(i) for i in input().split()]

for i in range(0,len(n)-1,2):
    if len(n)%2!=0 and i==(len(n)-1):
        break
    else:
        n[i],n[i+1] = n[i+1],n[i]
        
print(' '.join([str(i) for i in n]))

# 9. Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list.

n = [int(i) for i in input().split()]

l,m = 0,0

for i in range(1,len(n)):
    if n[i] > n[l]:
        l = i
    elif n[i] < n[m]:
        m = i

n[l],n[m] = n[m],n[l]

print(' '.join(str(i) for i in n))

# 10. Given a list of numbers, count how many element pairs have the same value (are equal). 
# Any two elements that are equal to each other should be counted exactly once.

n = [int(i) for i in input().split()]
ctr = 0
for i in range(0,len(n)-1):
    for j in range(i+1,len(n)):
        if n[i] == n[j]:
            ctr +=1
print(ctr)

# 11. Given a list of numbers, find and print the elements that appear in the list only once. 
# The elements must be printed in the order in which they occur in the original list.

n = [int(i) for i in input().split()]
u = []
for i in range(len(n)):
    f = 0
    for j in range(len(n)):
        if n[i] == n[j]:
            f += 1
    if f <= 1:
        u.append(int(n[i]))
print(' '.join(str(i) for i in u))

# 12. In chess it is known that it is possible to place 8 queens on an 8×8 chess board such that none of them can attack another. 
# Given a placement of 8 queens on the board, determine if there is a pair of queens that can attach each other on the next move. 
# Print the word NO if no queen can attack another, otherwise print YES. 
# The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chess board 
# with rows and columns numbered starting at 1.

queens = []
queens = []
i,l = 0,8
while i in range(l):
    queens.append(input())
    i+=1

flag = 0
for a in range(l):
    q1_x,q1_y = int(queens[a][0]),int(queens[a][2])
    for b in range(a+1,l):
        q2_x,q2_y = int(queens[b][0]),int(queens[b][2])
        if q1_x == q2_x or q1_y == q2_y or (abs(q1_x-q2_x) == abs(q1_y-q2_y)):
            flag = 1
if flag==1:
    print("YES")
else:
    print("NO") 