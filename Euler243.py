import time
def is_resilient(numer,denom):
    number=numer
    for num in range(2,9):
        if(numer>denom-(denom/num)):
            number=denom/num
    for i in range(2,number+1):
        if numer%i==0:
            if denom%i==0:
                return False
    return True
def resilient_fraction(denominator):
    resilient=0
    for num in range(1,denominator):
        if(is_resilient(num,denominator)):
            print num
            resilient+=1
    return str(resilient)+"/"+str(denominator-1)
start=time.clock()
print resilient_fraction(94745)
stop=time.clock()
print stop-start
