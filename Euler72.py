import time
def is_proper(numer,denom):
    for i in range(2,numer+1):
        if numer%i==0:
            if denom%i==0:
                return False
    return True
def proper_fraction(denominator):
    proper=0
    for num in range(1,denominator):
        if(is_proper(num,denominator)):
            proper+=1
    return proper
start=time.clock()
total=0
for denominator in range(1,1001):
    total+=proper_fraction(denominator)
print "number of reduced proper fractions: "+str(total)
stop=time.clock()
print stop-start
