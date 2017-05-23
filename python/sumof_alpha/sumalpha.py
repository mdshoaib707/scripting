import sys

arr=[]

for value in xrange(1,len(sys.argv)):
    arr.append(sys.argv[value].lower())

print arr

otharr=[]

def one():
    otharr.append(1)

def two():
    otharr.append(2)

def three():
    otharr.append(3)

def four():
    otharr.append(4)

def five():
    otharr.append(5)

def six():
    otharr.append(6)

def seven():
    otharr.append(7)

def eight():
    otharr.append(8)

def nine():
    otharr.append(9)

def ten():
    otharr.append(10)

options = {
    'one' : one,
    'two' : two,
    'three' : three,
    'four' : four,
    'five' : five,
    'six' : six,
    'seven' : seven,
    'eight' : eight,
    'nine' : nine,
    'ten' : ten
}

finalsum=0

for sum1 in arr:
    options[sum1]()

for add in otharr:
    finalsum=finalsum+add

print "Addition of ",arr, "=",finalsum
