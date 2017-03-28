import time
import sys
start=time.clock()
def listuptonum(n):
    return [i for i in xrange(1,n)]
lst=[1]*10001
lenlst=len(lst)
count=0
for index in xrange(2,lenlst):
    mult=index
    while(mult<lenlst):
        lst[mult]+=index*index
        mult+=index
sum1=0
for num in xrange(1,lenlst):
    numexp=lst[num]**0.5
    if(round(numexp)==numexp):
        print "index: " + str(num)
        print "numexp: " + str(numexp)
        sum1+=num
print "sum: " + str(sum1)
print lst[246]
print lst[246]**0.5
print lst[42]**0.5
print sys.getsizeof(lst)
stop=time.clock()
print stop-start
"""for num in xrange(1,10001):
    sum1=num*num+1
    if(num%2==0):
        for divisor in xrange(2,int(num**0.5)+1):
            if(num%divisor==0):
                sum1+=divisor*divisor
                if(divisor*divisor!=num):
                    sum1+=(num/divisor)**2
    else:
        for divisor in xrange(3,int(num**0.5)+1,1):
            if(num%divisor==0):
                sum1+=divisor*divisor
                if(divisor*divisor!=num):
                    sum1+=(num/divisor)**2
    sum1exp=sum1**0.5
if(round(sum1exp)==sum1exp):
    print "num: " + str(num)
    print "sum: " + str(sum1)
    print "sum1exp: " + str(sum1exp)"""
