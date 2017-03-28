import time
start=time.clock()
primes=[True]*7071
realprimes=[]
uniquenums=[]
count=0
primes[0]=False
primes[1]=False
for index in range(2,len(primes)):
    if(primes[index]):
        index2=index*2
        while(index2<len(primes)):
            primes[index2]=False
            index2+=index
for prime in range(0,len(primes)):
    if(primes[prime]):
        realprimes.append(prime)
for num in realprimes[0:100]:
    for num2 in realprimes[0:150]:
        for num3 in realprimes:
            if num**4+num2**3+num3*num3<50000000:
                uniquenums.append(num**4+num2**3+num3*num3)
uniquenums=list(set(uniquenums))
count+=len(uniquenums)
print count
stop=time.clock()
print stop-start
