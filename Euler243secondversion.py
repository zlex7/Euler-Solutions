import time
start=time.clock()
realprimes=[]
primecomparison=[]
chainprimes=[]
count=0
def primelist(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
lst1=[1]*40000
lst2=[34343]*20000
start2=time.clock()
for num in lst1:
    for num2 in lst2:
        count+=1
    if(count%100==0):
        print count
stop2=time.clock()
print stop2-start2
print count
stop=time.clock()
print stop-start
