import time
count=10
count2=0
s=""
digitsum=[]
def sum_digits(num):
    if num<10:
        return num
    return num%10 + sum_digits(num//10)
start=time.clock()
while(count2<12):
    sumofdigits=sum_digits(count)
    if(count%sumofdigits==0):
        for power in range(2,7):
            if sumofdigits**power==count:
                print "count: " + str(count)
                print "sumofdigits: " + str(sumofdigits)
                print "power: " + str(power)
                count2+=1
                break
    count+=1
stop=time.clock()
print stop-start
