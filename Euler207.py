import math
import time

def get_factors(num):
    factors=[]
    for i in xrange(0,num**0.5):
        if(num%i==0):
            factors.append(i)
            factors.append(num/i)
    if(num%(num**0.5)==0):
        factors.append(num**0.5)
    return factors
def get_factors_addtonegative1(num):
    sqrt = num**0.5
    up = math.ceil(sqrt)
    down = math.floor(sqrt)
    if(up-down==1):
        if(up*down==num):
            return up
    else:
        #print "no factors with difference of -1"
        return None
start=time.clock()
xTotal=0.0
xIntegers=0.0
print(1.0/12345.0)
boolean=True
k=1
lastxInteger=0
lastkInteger=1
function="2^(2x)-2^x-k"
lastPercentK=1.0
ratio=1.0/3.0
numerator=2.0
denominator=3.0
powerof2=3.0
ratio=2./3.
k=12.0
intX = []
intX.append(2)
intX.append(12)

for num in xrange(10):
    print num
while(k<100000000000):
    ratio=(numerator/denominator)*ratio
    k=k*4+2**powerof2
    if(ratio==1.0/12345.0):
        print "answer: " + str(k)
        break
    powerof2+=1
    numerator+=1
    denominator+=1
    intX.append(k)
totalMatches=0.0
ind=0.0
integerMatches=0.0
fraction=1.0/12345.0
for num in intX:
    totalMatches+=2.0**ind
    integerMatches+=1
    print "integerMatches: " + str(integerMatches)
    print "totalMatches: " + str(totalMatches)
    print(integerMatches/totalMatches)
    print(ind)
    print(intX[int(ind)])
    if(integerMatches/totalMatches<fraction):
        print("answer: " + str(num))
        break
    if(num==17179738112):
        num2=num+1
        lastnum=0
        increment=262144
        while(totalMatches<=209865):
            num+=increment
            increment+=2
            totalMatches+=1
        print "FINAL ANSWER: " + str(num)
        break
        print "ratio: " + str(integerMatches/totalMatches)
        while(totalMatches<131100):
            if(get_factors_addtonegative1(num2)):
                totalMatches+=1
                print totalMatches
                print num2-lastnum
                lastnum=num2
            if(totalMatches==209865):
                print "ANSWER: " + str(num2)
                break
            num2+=1
    ind+=1
    """
k=1.0
count=0.0
intCount=0.0
index=0
fraction=1.0/12345.0
while(boolean):
    factor = get_factors_addtonegative1(k)
    #print k
    if(factor):
        count+=1
        if k==intX[index]:
            intCount+=1
            print "k: " + str(k)
            print "total matches: " + str(count)
            print "integer matches: " + str(intCount)
            print "ratio: " + str(intCount/count)
            index+=1
        if(intCount/count==fraction):
            print "answer: " + str(k)
            break
    k+=1
        


        x=math.log(factor,2.0)
        xTotal+=1
        if(x==int(x)):
            xIntegers+=1
            print "k: " + str(k)
            print "x: " + str(x)
            print("xTotal: " + str(xTotal))
            print "ratio: " + str(xIntegers/xTotal)
            #if(lastxInteger!=0):
             #   print "percent change of ratio: " + str((xIntegers/xTotal)/lastxInteger)
            #print "percent change of k: " + str(float(k)/lastkInteger)
            #print "percent change of percent change of k: " + str(lastPercentK/(float(k)/lastkInteger))
            #lastPercentK=float(k)/lastkInteger
            lastxInteger=xIntegers/xTotal
            lastkInteger=k
        
        if(xTotal>100000):
            print "greater than 100000"
            if(xIntegers/xTotal==1.0/12345.0):
                print "answer: " + str(k)
                break
    
    k+=1
"""
"""
ratio=1.0/3.0
numerator=2.0
denominator=3.0
powerof2=3.0
ratio=2./3.
k=12.0
while(boolean):
    print "k: " + str(k)
    print("ratio: " + str(ratio))
    ratio=(numerator/denominator)*ratio
    k=k*4+2**powerof2
    if(ratio==1.0/12345.0):
        print "answer: " + str(k)
        break
    powerof2+=1
    numerator+=1
    denominator+=1
"""
stop=time.clock()
print stop-start

"""
arr = np.arange(12).reshape(3,4)

print arr
print arr.dtype
print arr.itemsize
print arr.sum(axis=0)
print arr.sum(axis=1)
"""

