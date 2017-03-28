import math
for num in xrange(5,100):
    print "num: " + str(num)
    sum1=0
    sum2=0
    count=1
    for num2 in xrange(num-5,num):
        #print "num2: " + str(num2)
        #print "number " + str(count) + ": " + str(math.factorial(num2)%num)
        sum1+=math.factorial(num2)
        count+=1
    print "answer: " + str(sum1%num)
    print "ginas theory: " + str((9*math.factorial(num-5))%num)
