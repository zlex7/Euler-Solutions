import time
start=time.clock()
lst = [0]*10000
realprimes=[]
answer=[]
def factors(num):
  lst=[]
  lst.append(1)
  lst.append(num)
  for i in xrange(2,int(num**0.5)+1):
    if num%i==0:
      lst.append(i)
      if(num/i!=i):
        lst.append(num/i)
  return lst
lenlst=len(lst)
for index in range(2,len(lst)):
  if(not lst[index]):
    realprimes.append(index)
  index2=index*2
  while(index2<lenlst):
    lst[index2]=1
    index2+=index
print len(realprimes)
print realprimes[2]
for index in xrange(2,len(realprimes)-1):
  #print"index: " + str(index)
  num = realprimes[index]
  multnum=10**len(str(num))
  num2=realprimes[index+1]*2
  num3=num2/2
  print "prime 1: " + str(num)
  print "prime 2: " + str(num2/2)
  while(num3%multnum!=num):
    num3+=num2
  print "answer: " + str(num3)
  print "factors: " + str(factors(num3))
  #answer.append(num3)
#print answer
  #print "answer: " + str(num3)
stop=time.clock()
print stop-start
      
    
