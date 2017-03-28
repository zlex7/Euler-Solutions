import time
start=time.clock()
primes=[True]*1000000
realprimes=[]
count=0
primes[0]=False
primes[1]=False
print 9.0**(1./3)
for index in range(2,len(primes)):
    if(primes[index]):
        index2=index*2
        realprimes.append(float(index))
        while(index2<len(primes)):
            primes[index2]=False
            index2+=index
print len(realprimes)
for num in range(1,601):
    cubic=(num+1)**3-(num**3)
    for num2 in realprimes:
        if num2==cubic:
            count+=1
            break
print count
stop=time.clock()
print stop-start
