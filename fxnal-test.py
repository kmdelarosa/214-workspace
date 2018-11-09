def calc(f,x,y):
    return f(x,y)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

calc(add,10,20)
calc(sub,20,10)

calc(lambda x, y: x+y,10,20)
calc(lambda x, y: x-y,20,10)

# Sample 1

def incr(x):
    return x+1

# Procedural version
def increment_each(elements):
    result = []
    for elem in elements:
        result.append(incr(elem))
    return result

increment_each([1,2,3])

# Functional version

# map takes a function and an iterable, loops through the iterable, calling the function on each element, 
# packs the results into a new list, and returns the list

map(incr,[1,2,3])
map(lambda x: x+1,[1,2,3])

# Sample 2

elements = []
results = []

for elem in elements:
    results.append(len(elem))

map(len, elements)

# If map() was not a built in function

def map(fxn,elements):
    results = []
    for elem in elements:
        results.append(fxn(elem))
    return results

# Other similar functions for map()

filter(lambda x: x%2==0,[1,2,3,4,5]) # Return a new sequence where values are taken from the given sequence 
# -> 2,4                             # if the condition holds true

from functools import reduce

reduce(lambda accum, current: accum+current,[1,2,3],0) # Accumulate and returns a single result,
# -> 6                                                 # given a sequence and passing each value to a function
                                                       # along with the current result                                                                            
