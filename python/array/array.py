import sys

arr=[]

for conv in range(1,len(sys.argv)):
    arr.append(float(sys.argv[conv]))

print "Entered array is: ", arr

sum=0

for value in arr:
    sum=sum+value

print "Sum of ", arr ," is: ", sum
