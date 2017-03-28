import time
start=time.clock()
realprimes=[]
primecomparison=[]
primecomparison2=[]
chainprimes=[]
count=0
def primelist(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
start2=time.clock()
primecomparison=primelist(10000000)
for prime in primecomparison:
    realprimes.append([prime-1,1,prime])
stop2=time.clock()
print stop2-start2
print len(realprimes)
print len(primecomparison)
lenrealprimes=len(realprimes)
for p in primecomparison[600000:605000]:
    for array in realprimes[1100000:1200000]:
        if(array[0]%p==0):
            print "p: " + str(p)
            print array[0]
            array[0]/=p
            array[1]+=1
print realprimes[len(realprimes)/2+500][0]
for prime in primecomparison[0:600000]:
    print prime
    for primearray in realprimes:
        if(primearray[0]==1):
            if(primearray[1]==10):
                chainprimes.append(primearray[2])
                continue
        else:
            primecomparison2.append(primearray)
        while(primearray[0]%prime==0):
            primearray[0]/=prime
            primearray[1]+=1
    realprimes=primecomparison2
    primecomparison2=[]
    print "length: " + str(len(realprimes))
#for primearray in realprimes:
    #if primearray[1]!=25:
      #  realprimes.remove(primearray)
print chainprimes
print len(chainprimes)
print count
stop=time.clock()
print stop-start
