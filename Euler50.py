import time
primes=[True]*300000
primestomil=[True]*1000000
realprimes=[]
realprimes2=[]
finallist=[]
finallist2=[]
number=0
stop=time.clock()
mil=False
for index in range(2,len(primes)):
    if(primes[index]):
        index2=index*2
        realprimes.append(index)
        while(index2<len(primes)):
            primes[index2]=False
            index2+=index
stop2=time.clock()
for index3 in range(2,len(primestomil)):
    if(primestomil[index3]):
        index4=index3*2
        realprimes2.append(index3)
        while(index4<len(primestomil)):
            primestomil[index4]=False
            index4+=index3
start2=time.clock()
print start2-stop2
print(len(realprimes))
for index in range(0,len(realprimes)):   
    count=realprimes[index]
    num=1
    for index2 in range(index+1,len(realprimes)):
        count+=realprimes[index2]
        num+=1
        if(count>=1000000):
            break
        if(primestomil[count]):
            finallist.append((count, num))
print("length of finallist: " + str(len(finallist)))
print("last element of finallist: " +str(finallist[0]))
print("length of finallist2: " + str(len(finallist2)))
number=0
count2=0
for array in finallist:
    if(array[1]>count2):
        count2=array[1]
        number= array[0]
print("end results")
print(count2)
print(number)
start=time.clock()
print(start-stop)
