import time
def primelist(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
indexes=[]
def primelist2(n):
    primes=[True]*n
    realprimes=[]
    extras=[]
    for index in range(2,len(primes)):
        if(primes[index]):
            index2=index*2
            realprimes.append(index)
            if(index<10000):
                if(100000000/index==10238):
                    print "fdfsdfs: " + str(index)
                extras.append(100000000/index)
            else:
                for extra in extras[::-1]:
                    if(extra-index>0 and extra-index<100):
                        print "index: " + str(index)
                        indexes.append(len(realprimes))
                        extras.remove(extra)
            while(index2<len(primes)):
                primes[index2]=False
                index2+=index
    print "extras length: " + str(len(extras))
    print extras
    return realprimes
print(100000000**0.5)
start=time.clock()
print(100000000/2)
primes2=primelist2(10000)
primes=primelist2(1000000)
count=0
answers=[]
for prime in range(0,len(primes2)):
    for prime2 in range(prime,len(primes2)):
        if(primes2[prime]*primes2[prime2]<100000000):
            count+=1
primes2.reverse()
i=0
print "indexes: " + str(len(indexes))
print len(primes2)
print len(primes)
#print indexes
for num in primes2:
    count+=indexes[i]-10000
    i+=1
    
print("math: " + str(((len(primes)*(len(primes)-1))/2)+len(primes)))
print("count: " + str(count))
print(len(primes))
stop=time.clock()
print(stop-start)
