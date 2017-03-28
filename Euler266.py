import time
start=time.clock()
lst = [0]*190
realprimes=[]
answer=[]
for index in range(2,len(lst)):
    if(not lst[index]):
        realprimes.append(index)
    index2=index*2
    while(index2<len(lst)):
        lst[index2]=1
        index2+=index
s=1
for num in realprimes:
    s*=num
print s
def pseudo_square(num):
    root=int(num**0.5)
    while(root>0):
        if(num%root==0):
            return root
        root-=1
        print root
print(pseudo_square(3102))
stop=time.clock()
print stop-start
