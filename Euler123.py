import time

start=time.clock()
numbers = [0]*1000000
primes=[]
for num in xrange(2,len(numbers)):
    if(not numbers[num]):
        primes.append(num)
        num2=num
        while(num2<len(numbers)):
            numbers[num2]=1
            num2+=num

for num in range(10,1):
    print num
for num in xrange(1,len(primes)/1000+1):
    temp = primes[num-1]
    first = temp-1
    second = temp+1
    third = temp*temp

    binary = format(num,'b')
    powers = []

    count=0
    
    for index in range(len(binary)-1,-1,-1):
        char = binary[index]
        if(char=='1'):
            powers.append(2**count)
        count+=1
    print powers
    #for power in powers:
        
stop=time.clock()
print(len(primes))
print(numbers[4])
print(stop-start)
